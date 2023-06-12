from PyKomoran import *
import fasttext
from konlpy.tag import Okt

level_dict = {"💡아이디어":{"💻프로그래밍":0,"📖소재":1,"🧶잡생각":2},
              "☑️할일":{"📔학교":0,"🏠집":1,"🔥대외활동":2,"👞회사&알바":3},
              "🤓정보":{"🍽️맛집":0,"🍯꿀팁":1,"🚩핫플레이스":2,"🎫문화생활":3},
              "📌기억할것":{"❗피드백":0,"🎯추천리스트":1,"😎임무":2,"📢중요":3},
              "🔮위시리스트":{"🎥미디어":0,"🍔먹킷리스트":1,"🛒쇼핑리스트":2,"📝버킷리스트":3}}

def leveling(result_list):
    if result_list[0] in list(level_dict.keys()):
        return result_list
    actual_result = [result_list[1], result_list[0],result_list[-1]]
    
    return actual_result

def w2v(userMemo):

    okt = Okt()
    MemoMorph= okt.morphs(userMemo)

    return " ".join(MemoMorph[i] for i in range(len(MemoMorph)))

def a(userMemo):

    input_morph = w2v(userMemo)

    model = fasttext.load_model('./V1.bin')

    result = model.predict(input_morph,k=2)
    
    model_result = [result[0][0].split('__')[-1], result[0][1].split('__')[-1], userMemo]

    return leveling(model_result)