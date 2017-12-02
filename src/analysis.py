import random
from janome.tokenizer import Tokenizer
from rhyme import rhymes

ok_words = ["名詞", "動詞", "形容詞"]


class Mor_analysis:

    def __init__(self, text):
        self.text = text
        self.t = Tokenizer()
        self.tokens = self.t.tokenize(self.text)
        for i in self.tokens:
            print(i)

    def divide_pos(self):
        """
        入力された文を品詞で分けて,名詞,動詞,形容詞を取り出しリストで返す
        => return (List, List, dict)
        """
        accept = []
        accept_attr = {}  # 品詞
        accept_index = []  # index

        for i, token in enumerate(self.tokens):
            part_of_speech = token.part_of_speech.split(",")[0]
            base_form = token.base_form
            if part_of_speech in ok_words:
                accept.append(base_form)
                accept_attr[base_form] = part_of_speech
                accept_index.append(i)
            else:
                self.tokens[i] = self.tokens[i].base_form

        print(accept, accept_index)
        return accept, accept_index, accept_attr

    def divide_attribute(self, attr_list, target):
        """ 同じ属性(品詞)を持つものに分ける """
        res = []

        for i in attr_list:
            tokens = self.t.tokenize(i)
            for j in tokens:
                if target == j.part_of_speech.split(",")[0]:
                    # print(target, j.part_of_speech)
                    res.append(i)
        return res

    def make_text(self):
        """ textを生成して返す """
        accept, accept_index, accept_attr = self.divide_pos()
        print(accept, accept_index)
        f = False  # 変更されたかを確認するためのフラグ
        for i, j in zip(accept, accept_index):
            words = self.divide_attribute(rhymes(i), accept_attr[i])
            if len(words):
                f = True
                self.tokens[j] = random.choice(words)  # ランダムで選んで入れる

        try:
            res = "".join(self.tokens)
            if not f:
                return ""
            elif res == self.text:
                return ""
            else:
                print(self.tokens)
                return res
        except TypeError:
            return ""


if __name__ == "__main__":
    a = Mor_analysis(__import__("sys").argv[1])
    print(a.make_text())
