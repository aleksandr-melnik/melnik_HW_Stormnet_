class Pismo_DedMoroz:
    def __init__(self, name, good_behavior, presents=None):
        self.name=name
        self.good_behavior = True
        self.presents = []
    @staticmethod
    def letter_generation():
        good_behavior=True
        presents = ['магнитофон', 'кинокамера', 'портсигар отечественный', 'куртка замшевая']
        while good_behavior:
            answer = bool(input('Ты хорошо себя вел: Да/Нет: '))
            if answer == 'Да':
                good_behavior=True
            else:
                good_behavior = False

    @staticmethod
    def dump_to_file():
        answer = False
        name = str(input('Как тебя зовут?'))
        presents = 'магнитофон, кинокамера, портсигар отечественный, куртка замшевая'
        letter_dedmoroz = open("letter_dedmoroz.txt", "w", encoding='utf-8')
        if answer == 'Да':
            letter_dedmoroz.write('Дорогой {0}, ты хорошо себя вел в этом году и получаешь {1}.'.format(name, presents))
        else:
            letter_dedmoroz.write('Дорогой %s, ты плохо себя вел в этом году и ничего не получаешь.' % name)
            letter_dedmoroz.close()
            return name
if __name__ == '__main__':
    Pismo_DedMoroz.letter_generation()
    Pismo_DedMoroz.dump_to_file()
    print('Письмо от %s отправлено' %Pismo_DedMoroz.__name__)