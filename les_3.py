# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом из набора 3 детали.
# Какова вероятность того, что все изъятые окрашенные детали?

импортировать  numpy
импорт  ОС


если  __name__  ==  '__main__' :
    ос . система ( 'клс' )

    ЧАСТИ  =  15
    ОКРАШЕННЫЕ_ЧАСТИ  =  9
    НЕОБХОДИМО_ЧАСТИ  =  3

    m_favorable_outcomes  =  numpy . математика . гребень ( PAINTED_PARTS , НЕОБХОДИМО_ЧАСТЕЙ )
    n_total_outcomes  =  numpy . математика . гребень ( ДЕТАЛИ , НЕОБХОДИМО_ЧАСТЕЙ )
    вероятностное_событие  =  числовое значение . разделить ( m_favorable_outcomes , n_total_outcomes )

    result_task  =  'Вероятность того, что извлекается случайным образом' \
        +  f'3 детали осуществяющихся окрашены p = { вероятность_события :.5f } '
    печать ( результат_задачи )
    # результат_задачи = 0,18462