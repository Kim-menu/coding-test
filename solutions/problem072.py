def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    word_stack = []
    answer = 0
    cur_word = ''.join(word_stack)
    while word != cur_word:
        if len(word_stack) < 5:
            word_stack.append('A')
        else:
            last_char_idx = vowel.index(word_stack.pop())
            while word_stack and last_char_idx == 4:
                last_char_idx = vowel.index(word_stack.pop())
            if word_stack or last_char_idx < 4:
                word_stack.append(vowel[last_char_idx+1])
            else:
                break
        cur_word = ''.join(word_stack)
        answer += 1
    return answer