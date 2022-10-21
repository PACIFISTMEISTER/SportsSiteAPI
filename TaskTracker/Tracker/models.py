from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from rest_framework.exceptions import ValidationError


class Player(models.Model):
    """информация о игроке"""
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Earingngs = models.PositiveIntegerField(default=0)
    MatchesPlayed = models.PositiveSmallIntegerField(default=0)
    PlayerCommand = models.ForeignKey('Command', on_delete=models.SET_NULL, related_name='PlayerCommand', blank=True,
                                      null=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['id']

class Command(models.Model):
    """информация о команде"""
    Name = models.CharField(max_length=50, unique=True)
    Wins = models.PositiveSmallIntegerField()
    CurrentOpponent = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)

    def CheckWins(self):
        if self.Wins is None:
            self.Wins = 0

    def clean(self):
        if Command.objects.filter(id=self.id).exists():
            if self.CurrentOpponent:
                if Command.objects.get(id=self.id) == Command.objects.get(id=self.CurrentOpponent.id):
                    raise ValidationError("u cant fight yourself")
                Command.objects.filter(id=self.CurrentOpponent.id).update(CurrentOpponent=self.id)

                if Match.objects.filter(Q(CommandOne=self) | Q(CommandTwo=self),
                                        IsActive=True).exists() or Match.objects.filter(
                    Q(CommandOne=self.CurrentOpponent) | Q(CommandTwo=self.CurrentOpponent),
                    IsActive=True).exists():
                    raise ValidationError("one of the teams has going match")
                mtch = Match(CommandOne=self, CommandTwo=self.CurrentOpponent, Price=0, IsActive=True)
                mtch.save()
            else:
                if Match.objects.filter(Q(CommandOne=self) | Q(CommandTwo=self), IsActive=True).exists():
                    Match.objects.filter(Q(CommandOne=self) | Q(CommandTwo=self), IsActive=True).update(IsActive=False,
                                                                                                        Winner=self)

        return True

    def AfterSave(self):
        if self.CurrentOpponent:
            Command.objects.filter(id=self.CurrentOpponent.id).update(CurrentOpponent=self.id)
            if Match.objects.filter(
                    Q(CommandOne=self.CurrentOpponent) | Q(CommandTwo=self.CurrentOpponent),
                    IsActive=True).exists():
                raise ValidationError("one of the teams has going match")
            mtch = Match(CommandOne=self, CommandTwo=self.CurrentOpponent, Price=0, IsActive=True)
            mtch.save()

    def save(self, *args, **kwargs):
        self.CheckWins()
        st = 0
        if self._state.adding:
            st = 1
            # self.AfterSave()
        super().save(*args, **kwargs)
        if st == 1:
            self.AfterSave()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']


class Match(models.Model):
    """информация о матче"""
    CommandOne = models.ForeignKey(Command, on_delete=models.SET_NULL, related_name='CommandOne', blank=True,
                                   null=True)
    CommandTwo = models.ForeignKey(Command, on_delete=models.SET_NULL, related_name='CommandTwo', blank=True,
                                   null=True)
    Price = models.PositiveIntegerField()
    Date = models.DateTimeField(default=datetime.now)
    Winner = models.ForeignKey(Command, on_delete=models.SET_NULL, related_name='Winner', blank=True, null=True)
    IsActive = models.BooleanField(default=False)

    def clean(self):
        if self.CommandOne == self.CommandTwo:
            raise ValidationError("Commands are the same")
        if self.Winner:
            if self.Winner != self.CommandOne and self.Winner != self.CommandTwo:
                raise ValidationError("winner is not in the lobby")
        if self.Winner and self.IsActive == True:
            raise ValidationError("u cant have winner in active match")
        if self.IsActive == False and self.Winner is None:
            raise ValidationError("u must have winner in not active match")

        return True

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['Date']

    def __str__(self):
        return f'{self.CommandOne}--{self.CommandTwo} --{str(self.IsActive)}'


class Bet(models.Model):
    Amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='Command')
    Match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='Match')
    Payed = models.BooleanField(default=False)

    def clean(self):
        if self.Command != self.Match.CommandOne and self.Command != self.Match.CommandTwo:
            raise ValidationError("Commands are not in match")
        if Bet.objects.filter(user=self.user, Match=self.Match).exists():
            raise ValidationError("Bet has been already made")
        if self.Match.IsActive == False:
            raise ValidationError("u cant bet on ended matches")

        return True

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['Amount']

    def __str__(self):
        return f'{self.Command}-({self.Match})-{self.user.username}'
