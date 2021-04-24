"""
File to save constant values for positive tests
"""

ENGLISH_TEXT = "/function_tests/src/eng_file.txt"
SYMBOLS_FILE = '/function_tests/src/signs_file.txt'
EMPTY_FILE = '/function_tests/src/empty_file.txt'

LINES_LEN_VAL = [
    (
        5,[
            '\tFrom:Barcelona, Catalonia, Spain',
            '',
            '\tWeb designer: Abel Sutilo',
            '\tTwitter: @abelsutilo',
            '\tFrom:Sevilla, Andalucia, Spain'
        ]
    ),
    (-5, [
        '\tFrom:Barcelona, Catalonia, Spain',
        '',
        '\tWeb designer: Abel Sutilo',
        '\tTwitter: @abelsutilo',
        '\tFrom:Sevilla, Andalucia, Spain'
    ]
     ),
    (0,[
        '/* TEAM */',
        '\tChef:Juanjo Bernabeu',
        '\tContact: hello [at] humanstxt.org',
        '\tTwitter: @juanjobernabeu',
        '\tFrom:Barcelona, Catalonia, Spain',
        '',
        '\tUI developer: Maria Macias',
        '\tTwitter: @maria_ux',
        '\tFrom:Barcelona, Catalonia, Spain',
        '',
        '\tOne eyed illustrator: Carlos Mañas',
        '\tTwitter: @oneeyedman',
        '\tFrom:Madrid, Spain',
        '',
        '\tStandard Man: Abel Cabans',
        '\tTwitter: @abelcabans',
        '\tFrom:Barcelona, Catalonia, Spain',
        '',
        '\tWeb designer: Abel Sutilo',
        '\tTwitter: @abelsutilo',
        '\tFrom:Sevilla, Andalucia, Spain'
    ]
     )
]


MULTIPLE_LANGUAGES = [
    (
        "/function_tests/src/rus_file.txt",
        'ткуда был выслан в Варшаву под гласный надзор полиции за участие в революционных кружках[1].'
    ),
    (
        "/function_tests/src/jap_file.txt",
        '任那、加羅、秦韓六國諸軍事、安東大將軍、倭國王。至齊建元中，及梁武帝時，并來朝貢'
    )
]

EXPECTED_SYMBOLS_STR = "!.,/|\:;'\"[]{}?@^&$()*<>"
