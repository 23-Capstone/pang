from PyKomoran import *
import fasttext
from konlpy.tag import Okt

def a(userMemo):

    input_morph = w2v(userMemo)
    model = fasttext.train_supervised(input='./labeled_data.txt',
                                  epoch=5000,
                                  bucket=20000,
                                  lr=0.001,
                                  wordNgrams=2,
                                  dim=80,)

    model.save_model('./practice.bin')
    #print('Trained Completed !!')
    result = model.predict(input_morph,k=2)

    return [result[0][0].split('__')[-1], result[0][1].split('__')[-1], userMemo] 


def w2v(userMemo):

    okt = Okt()
    MemoMorph= okt.morphs(userMemo)

    return " ".join(MemoMorph[i] for i in range(len(MemoMorph)))