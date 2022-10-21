import itertools

from django.core.handlers.wsgi import WSGIRequest
from rest_framework import serializers
from django.db.models import Sum
from rest_framework.request import Request

from .models import Command, Player, Match, Bet


class PlayerSerialzier(serializers.ModelSerializer):
    """сериализатор игрока"""
    PlayerCommand = serializers.SerializerMethodField()

    def get_PlayerCommand(self, Player):
        if Player.PlayerCommand:
            name = Command.objects.get(id=Player.PlayerCommand.id)
            print(name)
            return name.Name
        else:
            return "no command"

    class Meta:
        model = Player
        fields = '__all__'


class CommandListSerializer(serializers.ModelSerializer):
    """сериализатор команд"""
    CurrentOpponent = serializers.SerializerMethodField()

    class Meta:
        model = Command
        fields = '__all__'

    def get_CurrentOpponent(self, Comm):
        if Comm.CurrentOpponent:
            name = Command.objects.get(id=Comm.CurrentOpponent.id)
            return name.Name
        else:
            return "no command"


class CommandSerialzer(serializers.ModelSerializer):
    """сериализатор команды"""
    players = PlayerSerialzier(many=True, source='PlayerCommand')

    class Meta:
        model = Command
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    """сериализатор матча"""
    CommandOne = CommandSerialzer(read_only=True)
    CommandTwo = CommandSerialzer(read_only=True)
    Winner = CommandSerialzer(read_only=True)
    IsActive = serializers.BooleanField(read_only=True)
    BetForFirst = serializers.SerializerMethodField()
    BetForSecond = serializers.SerializerMethodField()

    def get_BetForFirst(self, Match):
        sum = Bet.objects.filter(Match_id=Match.id, Command_id=Match.CommandOne).aggregate(Sum('Amount'))
        if sum['Amount__sum']:
            return sum['Amount__sum']
        else:
            return 0

    def get_BetForSecond(self, Match):
        sum = Bet.objects.filter(Match_id=Match.id, Command_id=Match.CommandTwo).aggregate(Sum('Amount'))
        if sum['Amount__sum']:
            return sum['Amount__sum']
        else:
            return 0

    class Meta:
        model = Match
        fields = '__all__'


class MatchesSerializer(serializers.ModelSerializer):
    """сериализатор матчей"""
    CommandOne = CommandListSerializer(read_only=True)
    CommandTwo = CommandListSerializer(read_only=True)
    Winner = CommandListSerializer(read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class CreateBet(serializers.ModelSerializer):
    """создание ставок"""
    command_choices = serializers.ChoiceField(choices=[], source='Command')

    class Meta:
        model = Bet
        fields = ('Amount', 'command_choices')

    def __init__(self, *args, **kwargs):
        """dynamic choices fields"""
        choice = Match.objects.filter(id=int(kwargs['context']['request'].get_full_path().split('/')[-2])).values_list(
            'CommandOne', 'CommandTwo')
        choice = itertools.chain(choice)
        super().__init__(*args, **kwargs)
        self.fields['command_choices'].choices = list(*choice)

    def create(self, validated_data):
        id_of_match = int(self.context['request'].get_full_path().split('/')[-2])
        bet = Bet.objects.create(user=self.context['request'].user, Match=Match.objects.filter(id=id_of_match).first(),
                                 Amount=validated_data['Amount'],
                                 Command=Command.objects.filter(id=validated_data['Command']).first())
        return bet


# class BetSerializer(serializers.ModelSerializer):
#     # Amount = serializers.IntegerField()
#     Command_choices = serializers.ChoiceField(choices=[])
#
#     class Meta:
#         model= Bet
#         exclude = ('Command', 'Match','user','Payed')
#
#     def __init__(self, *args, **kwargs):
#         """dynamic choices fields"""
#         choice = Match.objects.filter(id=int(kwargs['context']['request'].get_full_path().split('/')[-2])).values_list(
#             'CommandOne', 'CommandTwo')
#         choice = itertools.chain(choice)
#         super().__init__(*args, **kwargs)
#
#         self.fields['Command_choices'].choices = list(*choice)
#
#     def create(self, validated_data):
#         id_of_match = int(self.context['request'].get_full_path().split('/')[-2])
#         bet = Bet.objects.create(user=self.context['request'].user, Match=Match.objects.filter(id=id_of_match).first(),
#                                  Amount=validated_data['Amount'],
#                                  Command=Command.objects.filter(id=validated_data['Command_choices']).first())
#
#         return bet

class BetSerializer(serializers.ModelSerializer):
    """сериализатор ставки"""
    class Meta:
        model = Bet
        exclude = ('Match', 'user', 'Payed', 'id')

    def create(self, validated_data):
        id_of_match = int(self.context['request'].get_full_path().split('/')[-2])
        bet = Bet.objects.create(user=self.context['request'].user, Match=Match.objects.filter(id=id_of_match).first(),
                                 Amount=validated_data['Amount'],
                                 Command=validated_data['Command'])
        return bet
