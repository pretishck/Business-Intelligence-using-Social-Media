def word_tokenizer(sent):
        from nltk.tokenize import RegexpTokenizer

        emoticons = "[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
        real_numbers = "[+\-]?\d+[0123456789,/.:-]*%?"
        hashtags = "\#[\w_]+[\w\'_\-]*\w+"
        all_words = "[\w'\-_]*\w[\w'\-_]*"
        line_endings = "[.:;,!?]+"

        reg_string = emoticons+"|"+real_numbers+"|"+hashtags+"|"+all_words+"|"+line_endings
        word_tokenizer = RegexpTokenizer(reg_string)

        word_result = word_tokenizer.tokenize(sent)

        return word_result