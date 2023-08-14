text = 'Founded by Bruce McLaren in 1963, ' \
       'McLaren was on the path to building its first racecar in the first year.' \
       ' The first ever McLaren model was the McLaren M1A, which saw just 24 models produced. ' \
       'Later, the M1B emerged and entered the Can-Am championship,' \
       ' earning 43 victories and besting rival Porsche on the season. By 1965,' \
       ' McLaren had constructed their first Formula 1 entry, debuting at the legendary Monaco Grand Prix.'

words_in_test = text.split()
word = input('please enter the word you want to count: ')
times_repeated = int(0)

for each_word in words_in_test:
    if each_word == word:
        times_repeated = times_repeated+1

print(times_repeated)
