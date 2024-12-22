﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define aly = Character('Аля', color="#b52bd1", image="aly")
define prof = Character('Профессор', color="#0ecc47", image="prof")
define man = Character('Неизвестный мужчина', color="#808080", image="man")
define profNoName = Character('Неизвестный мужчина', color="#808080", image="prof")
define n = Character(None, kind=nvl)
define vald = Character('Вальдемар', color="#315cf6", image="vald")
define franz = Character('Франц', color="#f631ba", image="franz")
define vivi = Character('Вивиан', color="#26781c", image="vivi")
define voice = Character('Голос из динамика', color="#aa1414")
define android  = Character('Андроид', color="#14a1da")
image successhack = Movie(play="images/successhack.webm", size=(1920,1080), loop=False, xalign=0.10, yalign=0.10)
image failurehack = Movie(play="images/failurehack.webm", size=(1920,1080), loop=False, xalign=0.10, yalign=0.10)

init python:
    import random

    # Список путей к изображениям фрагментов
    fragment_images = [
        "images/mg/correct_fragment_1.jpg",
        "images/mg/correct_fragment_2.jpg",
        "images/mg/correct_fragment_3.jpg",
        "images/mg/correct_fragment_4.jpg",
        "images/mg/wrong_fragment_1.jpg",
        "images/mg/wrong_fragment_2.jpg",
        "images/mg/wrong_fragment_3.jpg",
        "images/mg/wrong_fragment_4.jpg",
    ]

    renpy.random.shuffle(fragment_images)

    # Состояния фрагментов
    for i in range(8):
        globals()["fragment_selected_%d" % i] = False

    # Функция для подсчета правильных фрагментов
    def count_correct_fragments():
        correct_count = 0
        for i in range(4):  # Проверяем только первые 4 фрагмента (правильные)
            if globals().get("fragment_selected_%d" % i, False):
                correct_count += 1
        return correct_count

# Экран игры с кнопкой "Взлом"
screen hacking_game:
    modal True
    window:
        xalign 0.5
        yalign 0.5
        background "images/mg/bg fingerprint.jpg"
        xsize 1920  # Размеры окна (фона)
        ysize 1080

    # Отображение фрагментов
    vbox:
        spacing 10  # Расстояние между фрагментами
        xalign 0.3  # Перемещаем влево (меняем xalign)
        yalign 0.5  # Центрируем по Y
        grid 2 4:  # Создаём сетку с 2 колонками и 4 строками
            for i, fragment_path in enumerate(fragment_images):  # Перебираем изображения
                # Определяем выбранность фрагмента
                $ fragment_selected = globals().get("fragment_selected_%d" % i, False)
        
                imagebutton:
                    idle fragment_path  # Отображение изображения
                    hover At(
                        Composite(
                            (77, 77),  # Размер (подгоните под ваше изображение)
                            (0, 0), fragment_path,  # Слоями: базовое изображение
                            (0, 0), Solid("#ffffff80"),  # Светло-белый прозрачный наложенный слой
                        )
                    )
                    selected_idle At(
                        Composite(
                            (77, 77), 
                            (0, 0), fragment_path,
                            (0, 0), Solid("#ff808080"),  # Красноватый прозрачный слой
                        )
                    )
                    selected_hover At(
                        Composite(
                            (77, 77), 
                            (0, 0), fragment_path,
                            (0, 0), Solid("#ff666680"),  # Более яркий красный прозрачный слой
                        )
                    )
                    xsize 77  # Размер фрагмента (настройте под свои нужды)
                    ysize 77
                    action ToggleVariable("fragment_selected_%d" % i)  # Переключение состояния

    # Кнопка "Взлом"
    imagebutton:
        idle "images/mg/hack_button.png"
        hover At(
        Transform("images/mg/hack_button.png", size=(110, 110), alpha=0.5)  # Полупрозрачный слой
        )
        xalign 0.95  # Положение кнопки по горизонтали
        yalign 0.95  # Положение кнопки по вертикали
        action Function(check_hacking)

label hacking_game_success:
    hide screen hacking_game
    scene bg successhack
    show successhack

    aly "Получилось!!"

    scene bg server with fade

    show aly confusion at left

    show prof normal at right

    show android at center

    'Андроид остановился, его глаза потухли.'
    hide android with dissolve

    show aly scary with dissolve

    aly "Профессор! Я так испугалась..."

    prof alarm "Извини, Аля. Ты в порядке?"

    aly thinking "Да, кажется, всё хорошо. Что это за место?"

    prof serious "Пойдём, я всё объясню."
    stop music fadeout(1.0)

    scene bg corridor with fade
    play music "music/Office_Music.mp3" fadein(1.0)

    'Они вышли из помещения, и дверь снова закрылась за ними. Они остановились у большого окна, из которого открывался вид на город.'
    
    show aly normal at left with dissolve

    show prof normal at right with dissolve
    
    aly thinking "Профессор, это был... робот? Настоящий андроид?"

    prof normal "Да. Ты попала в наш самый секретный отдел. Проект 'Искра' — это разработка искусственного интеллекта нового поколения."

    aly happy "Невероятно! Он выглядит как человек! И говорит, и двигается..."

    prof normal "Мы стремимся создать ИИ, способный не только выполнять команды, но и думать, учиться, чувствовать."

    aly happy "Это потрясающе. Но почему такая секретность?"

    prof serious "Проект очень важен и потенциально опасен, если попадёт не в те руки. Поэтому мы тщательно охраняем его."

    aly confusion "Понимаю. Извините, что вошла без разрешения."

    prof normal "Всё в порядке. Главное, что ты не пострадала. Но, пожалуйста, никому об этом не рассказывай."

    aly normal "Обещаю. Ваш секрет — в надёжных руках."
    
    jump Chapter_7

    

label hacking_game_failure:
    hide screen hacking_game
    scene bg failedhack
    show failurehack
    "Неудачная попытка взлома. Хотите попробовать ещё раз?"
    menu:
        "Да":
            jump start_hacking_game
        "Нет":
            return

    

# Функция для проверки взлома
init python:
    def check_hacking():
        correct_count = count_correct_fragments()
        if correct_count >= 3:
            renpy.jump("hacking_game_success")
        else:
            renpy.jump("hacking_game_failure")

label start_hacking_game:
    show screen hacking_game
    window hide  # Убираем окно с текстом
    
    $ renpy.pause(2)  # Пауза на 2 секунды, чтобы игрок ничего не видел
    window show  # Показываем окно текста снова, если необходимо
    
    return


init python:
    style.default.justify=True

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')



label splashscreen:
    scene black with dissolve
    pause 1
    show text "Студия Крутые перцы" with dissolve
    pause 2
    show text "Представляет" with dissolve
    pause 2
    show text "Учебный проект" with dissolve
    pause 2 
    show text "Визуальная новелла" with dissolve
    pause 1
    return



# Игра начинается здесь:
# # НАЧАЛО 1 ГЛАВЫ
label start:

    scene bg school with fade 

    play music "music/Beginning.mp3"

    '''Вечерний воздух был пропитан запахом сырости и свежести, солнце садилось за горизонт, оставляя после себя пурпурные и оранжевые полосы на небе. 

    Аля, бросив взгляд на  небо, вспомнила сегодняшний урок проф.ориентации. Будущая профессия кажется ей такой неясной, ей нравиться программировать, но какие есть профессии, связанные с этим, она не знает.  

    Она мечтает работать в IT-индустрии, но какая именно специальность её привлекает, Аля не знает. Web-программист? DevOps? Специалист по кибербезопасности? Все эти профессии кажутся ей загадочными и недоступными. 

    Алю пугает мутное будущее.  
    '''
    jump credits 

    show aly scary at right with dissolve

    aly ''' Если я не буду получать удовольствие от работы, то я уйду с неё.

    А если я уйду с работы я перестану получать деньги, значит стану нищей.

    А если я стану нищей значит бездомной...  

    А если я стану бездомной, то...  
    '''
    with flashbulb

    '*Бум*' with hpunch
    
    # звук столкновения
    ''' Аля сталкивается.

    Аля замедлила шаг, и вдруг её ноги подкосились.

    Она споткнулась и упала, рассыпая по тротуару содержимое своей сумки: книги, тетради, зонт.
    '''

    aly normal "Извините."
    'Пробормотала Аля, поднимаясь и собирая рассыпанные вещи.'
    aly normal "Я не заметила вас… "

    ''' Мужчина с улыбкой помог ей собрать оставшиеся бумажки.

    Он был одет в очки в толстой оправе и простую темную куртку.

    Он смотрел на нее с забавно поднятой бровью.'''
     
    show prof normal at left with dissolve
    man normal "Ничего страшного."

    'Cказал он, в его голосе звучала спокойная уверенность.'

    profNoName "Произошло так произошло. А что у тебя случилось?"

    'Аля вздохнула, и в её голосе прозвучала безысходность.'
    
    aly scary "Я вот думаю, что будет дальше. Какая у меня будет профессия, как выбрать ту самую, из десятка других… Все так непонятно, будто в тумане."

    'Мужчина улыбнулся еще шире.'

    profNoName ''' Ничего страшного, я тебя понимаю. Все через это проходили. Но не стоит волноваться.

    Будущее не всегда прозрачно, и это нормально. Самое главное – не бояться делать первые шаги.

    Ты умная особа, и у тебя все получится. Нужно просто идти туда, где больше платят или куда душа лежит) '''

    aly thinking "Нуууу... Мне программирование нравится."
    prof normal "Отлично, нам как раз нужны новые кадры, меня зовут профессор, работаю в одной IT компании, не хочешь посмотреть, как мы работаем? "
    'Аля, размышляя над интересным предложением незнакомца, заметила бейдж с Брендингом “ТехноГрад”.'

    menu:
        "Предложение профессора."
        "Принять предложение профессора.":
            jump good_ending
        "Отказаться от предложения профессора.":
            jump bad_ending

label bad_ending:
    aly '''
    Простите, но я откажусь.

    Пускай я слышала о “ТехноГрад”, но я вас совсем не знаю.

    До свидания. 
    '''

    scene bg room with fade
    '''Вечером дома Аля сидела за своим ноутбуком. Перед ней светилась страница с курсами программирования.

    Она размышляла о предложении Профессора. 
    
    С одной стороны, это казалось невероятной возможностью, но с другой — она чувствовала неуверенность. Вопросы крутились в голове:'''

    aly "Могу ли я доверять человеку, которого только что встретила? {w}Что, если это слишком поспешное решение?"
    
    scene bg room with fade
    'На следующий день, вместо того чтобы пойти в “Техноград”, Аля осталась дома, продолжая готовится к экзаменам.'

    ''' Спустя несколько недель Аля всё ещё не могла найти мотивацию для своих проектов. 
    
    Её первоначальный энтузиазм угас, и она начала сомневаться в своих силах.
    
    Каждый день она пыталась начать что-то новое, но чувствовала, что ничего не получается.'''

    aly 'Почему я не могу довести дело до конца? {w}Может, я просто не создана для этого?'

    ''' Всё больше времени она проводила за просмотром видео о самых разных профессиях, но чем больше информации она получала, тем больше запутывалась.
    
    Её мысли были противоречивыми: 
    '''
    aly "IT — это интересно, но, может, попробовать что-то более творческое? {w}Или совсем уйти в науку? {w}А вдруг я просто трачу время впустую, пока мои сверстники уже знают, чем хотят заниматься?"

    '''Через несколько месяцев Аля, уставшая от неопределённости, решила поступить в университет на специальность, которую ей рекомендовали родители.
    
    Это была экономика — сфера, которая не вызывала у неё особого интереса, но казалась надёжной.

    Внутренний голос часто напоминал ей о её увлечении программированием, но она глушила эти мысли, убеждая себя, что сделала правильный выбор. 
    '''
    aly "Не все могут позволить себе мечтать." 

    'Убеждала она себя.'
    jump bad_epilogue

    
label bad_epilogue:
    '''Спустя год Аля училась на экономическом факультете. Её дни проходили в череде однообразных лекций и заданий.

    Она всё чаще вспоминала предложение Профессора и думала, как могла бы измениться её жизнь, неуверенности.

    В этом большом и непонятном мире программирования нашёлся человек, готовый помочь ей сделать первый шаг.'''
    return

label good_ending:
    'Аля вздрогнула, она узнала логотип компании на бейджике Профессора.'
    
    aly happy "Да, хочу. Но я еще не решила, кем хочу стать."
    prof normal "В таком случае, загляни завтра ко мне на работу, я постараюсь рассказать и показать тебе всё что знаю сам и может быть помогу тебе определиться ;)"

    'Аля немного успокоилась. Ей было приятно услышать эти слова от незнакомого человека.'
    aly happy "Спасибо."
    prof normal ''' Не за что.

    Я уже представился, а тебя как зовут?
    '''
    aly confusion "Аля."
    'Ответила она и улыбнулась.'

    prof normal 'Приятно познакомиться, Аля.'

    'Профессор улыбнулся и продолжил свой путь.'
    hide prof normal with dissolve

    'Аля еще некоторое время смотрела ему вслед, теперь в ее душе была не тревога, а надежда. '
  
    aly normal "Ещё раз спасибо, Профессор."
    'Прошептала она вслед уходящему человеку. С ниспадающей улыбкой направившись домой.'
    # КОНЕЦ 1 ГЛАВЫ
    stop music fadeout(1.0)

    jump Chapter_2


# НАЧАЛО 2 ГЛАВЫ
label Chapter_2:
    scene bg room with fade
    play music "music/during_the_dialogues.mp3" fadein(1.0)
    'Дома, уже в теплой комнате, Аля задумалась.'
    aly ''' “Техноград”… 
    
    Мне всегда нравилось как звучит это слово. 
    
    Может быть, предложение Профессора действительно поможет мне определиться с будущей профессией.

    Столько вопросов, но теперь есть надежда. 
    '''
    stop music fadeout(1.0)

    scene bg officecenter with fade
    play music "music/Office_Music.mp3"

    '''На следующее утро Аля с волнением подошла к офису "Технограда". 

    Высокое здание из стекла и металла возвышалось над городом, отражая лучи утреннего солнца.

    У входа её ждал Профессор. '''

    show prof normal at left with dissolve

    prof normal "Доброе утро, Аля! Рад, что ты пришла."

    show aly happy at right with dissolve
      
    aly confusion "Здравствуйте. Спасибо, что пригласили меня."

    prof normal "Пойдём, я проведу тебе экскурсию."

    # КОНЕЦ 2 ГЛАВЫ

    jump choose_office

    label choose_office:
        show bg corridor with fade
        if offices:
            if len(offices) == 1:
                $ office_name, office_label = offices.pop()
                "Нам осталось посетить только [office_name]."
                jump expression office_label
            else:
                "Куда ты хочешь пойти?"
                
                # Важно: нужно вручную добавить пункты в меню
                menu:
                    "Отдел геймдизайна" if ("Отдел геймдизайна", "Chapter_3") in offices:
                        $ offices.remove(("Отдел геймдизайна", "Chapter_3"))
                        jump Chapter_3
                    
                    "Отдел fullstack разработки" if ("Отдел fullstack разработки", "Chapter_4") in offices:
                        $ offices.remove(("Отдел fullstack разработки", "Chapter_4"))
                        jump Chapter_4

                    "Отдел тестировки" if ("Отдел тестировки", "Chapter_5") in offices:
                        $ offices.remove(("Отдел тестировки", "Chapter_5"))
                        jump Chapter_5
        else:
            jump Chapter_6

        
default offices = [
    ("Отдел геймдизайна", "Chapter_3"), 
    ("Отдел fullstack разработки", "Chapter_4"), 
    ("Отдел тестировки", "Chapter_5")
]


# НАЧАЛО 3 ГЛАВЫ
label Chapter_3:

    scene bg officeworkplace with fade

    show prof normal at center

    show aly happy at right

    prof "Для начала познакомлю тебя с Вальдемаром. Он глава отдела геймдизайнеров."

    'В кабинете их встретил энергичный мужчина с яркими глазами и растрепанными волосами.'
    stop music fadeout(1.0)

    play music "music/during_the_dialogues.mp3" fadein(1.0)
    show prof normal at left with move
    show vald normal at center
    vald smile "Привет, Профессор! А это кто у нас?"

    prof normal "Это Аля. Она интересуется IT, но ещё не определилась с направлением. Думаю, ты сможешь рассказать ей о геймдизайне."

    vald energy "С удовольствием!"

    aly confusion "Здравствуйте."

    vald smile "Не стесняйся! Проходи, располагайся. Геймдизайн — это невероятно захватывающая сфера."

    'Он жестом пригласил её к большому столу, заставленному эскизами, заметками и книгами.'

    hide prof normal

    show vald normal at left with move

    vald normal "Геймдизайнер — это тот, кто создаёт концепцию игры. Мы придумываем миры, механики, правила, персонажей, историю."

    vald normal "Наша задача — сделать игру интересной и увлекательной для игрока."

    aly normal "А с чего начинается процесс создания игры?"

    vald normal "Всё начинается с идеи. Это может быть что угодно: сюжет, механика, визуальный стиль. Затем мы разрабатываем гейм-дизайн-документ (GDD), в котором подробно описываем все аспекты игры."

    'Он показал ей толстую папку.'

    vald normal "Вот, например, GDD нашей текущей игры. Здесь описаны сюжет, персонажи, уровни, интерфейс, система прокачки и многое другое."

    aly happy "Ничего себе! Я и не думала, что всё так подробно прописывается."

    vald smile "Конечно! Это важно для всей команды — программистов, художников, аниматоров, звуковиков. Все должны понимать, что и как делать."

    'Он подвёл её к стене с концепт-артами.'

    vald normal "Здесь наши художники визуализируют идеи. Геймдизайнеры тесно сотрудничают с ними, чтобы создать уникальный и привлекательный мир."

    aly normal "А как вы придумываете механики игры?"

    vald normal "Мы изучаем разные жанры, анализируем успешные проекты, экспериментируем. Главное — понять, что понравится игрокам. Иногда мы создаём прототипы и тестируем их внутри команды."

    'Он включил компьютер и запустил прототип игры.'

    vald energy "Хочешь попробовать сыграть?"

    aly happy "С удовольствием!"

    'Она начала играть.'

    scene bg officeworkplace with fade
    show vald normal at left
    show aly normal at right

    aly confusion "Это действительно затягивает! А как вы понимаете, чего хотят игроки?"

    vald normal "Мы проводим исследования, опросы, следим за трендами в индустрии. Но иногда нужно просто довериться интуиции и творчеству."

    aly normal "Это очень интересно! Но, наверное, и сложно."

    vald normal "Безусловно. Но когда видишь, что твоя игра приносит радость людям, это того стоит."

    aly normal "А какие навыки нужны, чтобы стать геймдизайнером?"

    vald normal "Творческое мышление, аналитические способности, знание основ программирования и графики, умение работать в команде. И, конечно, любовь к играм."

    aly confusion "Спасибо большое за рассказ! Вы открыли для меня новый мир."

    vald smile "Рад был помочь. Если возникнут вопросы, не стесняйся обращаться."

    'Профессор, наблюдая за их беседой, подошёл ближе. '

    show prof normal at center with fade

    prof normal "Спасибо, Вальдемар. Нам пора идти дальше."

    aly happy "Ещё раз спасибо!"

    scene bg corridor with fade
    # КОНЕЦ 3 ГЛАВЫ

    jump choose_office

# НАЧАЛО 4 ГЛАВЫ
label Chapter_4:

    'Продолжая экскурсию, они подошли к следующему отделу. '

    show prof normal at center with dissolve

    "Теперь познакомлю тебя с Францем. Он руководит отделом Fullstack-разработки."

    scene bg fullstackoffice with fade

    'В кабинете царила тишина, лишь слышался тихий стук клавиш. За одним из столов сидел мужчина с сосредоточенным взглядом.'

    show prof normal at left with dissolve

    prof normal "Привет, Франц. Это Аля. Она интересуется программированием."

    'Франц поднял глаза.'

    show franz interested at center with dissolve

    franz interested "Здравствуйте."
    
    show aly confusion at right with dissolve

    aly confusion "Здравствуйте."

    hide prof normal

    show aly normal at right with move

    show franz confident at left with move

    franz confident "Интересуешься программированием? Что именно привлекает?"

    aly thinking "Хочу узнать больше о том, чем вы занимаетесь."

    'Франц отодвинул стул к ней.'

    franz normal  "Fullstack-разработчик — это специалист, который может работать как с фронтендом, так и с бэкендом приложения. Проще говоря, мы создаём как визуальную часть сайта или приложения, так и его серверную логику."

    aly thinking "А в чём разница между фронтендом и бэкендом?"

    franz focused "Фронтенд — это то, что видит пользователь: интерфейс, дизайн, взаимодействие с элементами на странице. Здесь используются языки HTML, CSS, JavaScript и различные фреймворки, такие как React или Angular."

    'Он показал ей на экране код страницы и открыл браузер с видом этой страницы.'

    franz focused "Бэкенд же отвечает за обработку данных, работу с базами данных, бизнес-логику приложения. Для этого используются языки, такие как Python, Java, PHP, а также базы данных — MySQL, PostgreSQL, MongoDB."

    'Он переключился на другой экран, где был написан серверный код.'

    aly happy "Получается, вы можете создавать полное приложение от начала до конца?"

    franz interested "Именно. Это позволяет лучше понимать всю систему, быстро вносить изменения и оптимизировать работу."

    aly thinking "А какие навыки нужны для этого?"

    franz normal "Хорошее знание языков программирования, понимание принципов построения сетевых приложений, умение работать с базами данных, знать основы безопасности. И, конечно, быть готовым постоянно учиться, так как технологии быстро развиваются."

    aly normal "Это звучит сложно, но увлекательно."

    franz interested "Хочешь попробовать написать небольшой код?"

    aly happy "Да, с удовольствием!"

    'Он уступил ей место за компьютером.'

    hide franz normal

    hide aly normal with fade
  
    scene bg fullstackoffice with fade

    show franz normal at left

    show aly normal at right

    aly happy "Это удивительно! Столько возможностей, и всё взаимосвязано. Я чувствую, как оживает то, что я создаю."

    franz interested "Отлично! Ты быстро учишься. Видишь, как фронтенд и бэкенд работают вместе?"

    aly happy "Да, спасибо большое! Это очень интересно."

    franz confident "Если хочешь развиваться в этом направлении, советую изучать алгоритмы, структуры данных, принципы объектно-ориентированного программирования. Также важно понимать архитектуру приложений и паттерны проектирования."

    aly normal "Обязательно. Я чувствую, что это моё."

    franz normal "Это хорошо. Программирование — это мощный инструмент творчества. Главное — не бояться сложностей."

    scene bg corridor with fade 
    # КОНЕЦ 4 ГЛАВЫ
    jump choose_office


# НАЧАЛО 5 ГЛАВЫ
label Chapter_5:
    play music "music/Office_Music.mp3" fadein(1.0)
    'Далее они отправились в отдел, заполненный всевозможными растениями и цветами.'

    scene bg qa with fade
    show aly happy at right with dissolve
    show prof normal at left with dissolve

    'Атмосфера здесь была совершенно иной: уютной и умиротворяющей. За столом с ноутбуком сидела девушка, окружённая растениями.'

    prof normal "Теперь познакомлю тебя с Виви. Она — наш ведущий тестировщик ПО."

    'За столом с ноутбуком сидела девушка с тёплой улыбкой. '
    stop music fadeout(1.0)
    
    play music "music/during_the_dialogues.mp3" fadein(1.0)
    show vivi normal at center with fade

    vivi happy "Привет! Ты, наверное, Аля?"

    hide prof normal

    show vivi normal at left with move

    aly confusion "Да. Здравствуйте. У вас здесь так красиво!"

    vivi normal "Спасибо! Растения помогают сосредоточиться и создают приятную атмосферу."

    aly thinking "Профессор сказал, что вы занимаетесь тестированием программного обеспечения?"

    vivi normal "Верно. Тестирование — это неотъемлемая часть разработки. Наша задача — найти ошибки, баги в приложении до того, как оно попадёт к пользователю."

    aly normal "А как вы это делаете?"

    vivi normal "Существует несколько видов тестирования: функциональное, интеграционное, нагрузочное, регрессионное и другие."

    vivi normal "Мы пишем тестовые сценарии — ситуации, в которых может оказаться пользователь, и проверяем, корректно ли работает приложение."

    'Она показала ей таблицу с тест-кейсами.'

    vivi normal "Вот здесь мы описываем шаги, ожидаемый результат и фактический результат. Если они не совпадают — это баг, и его нужно исправить."

    aly happy "Интересно! А какие инструменты вы используете?"

    vivi "Мы используем как ручное тестирование, так и автоматизированное с помощью специальных программ, таких как Selenium, JMeter, Postman для API-тестирования. Автоматизация позволяет быстро проверять большие объёмы функционала."

    aly normal "Получается, вы тоже программируете?"

    vivi normal "Да, для написания автотестов нужно знать языки программирования, чаще всего это Java, Python или JavaScript. Кроме того, важно понимать принципы работы приложений, чтобы эффективно находить уязвимости."

    aly happy "Это похоже на детективную работу!"

    vivi smile "Точно подмечено! Мы раскрываем тайны приложений и помогаем сделать их лучше."

    aly thinking "А как вы взаимодействуете с разработчиками?"

    vivi normal "Мы тесно сотрудничаем. После обнаружения бага, мы сообщаем о нём в системе отслеживания, например, Jira, подробно описывая проблему и как её воспроизвести. Разработчики исправляют, а мы затем проверяем, что всё работает корректно."

    'Вивиан посмотрела на Алю.'

    vivi satisfied "Хочешь попробовать самостоятельно провести тестирование?"

    aly happy "Да, конечно!"

    # МИНИ ИГРА

    vivi normal "Вот приложение, которое мы сейчас тестируем. Попробуй найти в нём недочёты."
    
    'Аля начала работать с приложением, внимательно изучая его функции. Спустя некоторое время она заметила, что при определённых действиях приложение ведёт себя некорректно.'

    scene bg qa with fade

    show aly happy at right

    show vivi normal at left

    aly happy "Кажется, я нашла баг! При нажатии этой кнопки приложение зависает."

    vivi smile "Отличная работа! У тебя зоркий глаз."

    aly confusion "Спасибо! Это действительно увлекательно."

    vivi normal "Тестировщик должен быть внимательным, усидчивым и уметь мыслить критически. Нужно предвидеть, как пользователь может сломать приложение, и предотвратить это."

    aly normal "Теперь я понимаю, насколько важна ваша работа."

    vivi happy "Да, мы — своеобразный последний рубеж перед выпуском продукта. От нас зависит качество и репутация компании."
    stop music fadeout(1.0)
    # КОНЕЦ 5 ГЛАВЫ

    scene bg corridor with fade 
    jump choose_office
    

#НАЧАЛО 6 ГЛАВЫ
label Chapter_6:
    
    scene bg corridor with dissolve
    play music "music/Office_Music.mp3" fadein(1.0)

    'После насыщенного дня Аля и Профессор вышли в центральный холл. Высокие потолки и панорамные окна создавали ощущение простора, а свет от люстр отражался на мраморном полу.'

    show prof normal at right with dissolve

    prof normal "Ну что, как тебе экскурсия?" 

    show aly happy at left with dissolve

    aly happy ''' Сегодня было столько нового и интересного!

    Я даже не могла представить, насколько разнообразен мир IT.

    Теперь мне гораздо легче понять, чем хочу заниматься. '''

    prof normal "И к какому выводу ты пришла?"

    aly thinking '''Мне понравилось всё.

    Но больше всего меня увлекла разработка. 

    Хочу стать Fullstack-разработчиком и создавать полезные приложения. Но и геймдизайн, и тестирование тоже интересны.

    Возможно, я смогу как-то объединить эти направления? '''

    prof normal "В современном мире многое становится взаимосвязанным. Твоё желание изучать несколько направлений только приветствуется."

    'Вдруг к ним подошёл мужчина в строгом костюме, держа в руках планшет'
    
    'Профессор, извините, что прерываю, но у нас срочное совещание. Вас уже ждут в зале заседаний.'

    prof alarm "Ах да, совершенно забыл. Спасибо, Олег. "

    prof normal "Аля, мне нужно идти. Ты можешь ещё немного погулять здесь или я провожу тебя к выходу?"
    
    aly normal "Не беспокойтесь, я сама доберусь. Хочу ещё немного осмотреться, если можно."

    prof normal "Конечно, чувствуй себя как дома. Только не заходи в помещения с пометкой 'Доступ ограничен'."

    aly normal "Обещаю следовать правилам."

    prof normal "Хорошо. Рад был помочь. Удачи тебе!"

    show aly normal

    hide prof normal with dissolve

    # НУЖЕН ФОН С ЛЕСТНИЦЕЙ И ОТКРЫТОЙ ДВЕРЬЮ, ВНУТРЕННОСТЯМИ КОМНАТЫ    
    'Он ушёл вместе с мужчиной, а Аля решила ещё немного осмотреться. '

    'Она бродила по коридорам, рассматривая картины на стенах и фотографируя интересные места.'
    stop music fadeout(1.0)
    
    scene bg stairs with fade
    play music "music/Final_boss_fight.mp3" fadein(1.0)
    '''Поднимаясь по лестнице, она заметила открытую дверь в зал с надписью "Проект 'Искра'". '''

    'Любопытство взяло верх, и она заглянула внутрь.'

    scene bg server with fade
    
    'В комнате стояли странные устройства: серверные стойки, мониторы с бегущими строками кода, мерцающие панели управления.' 

    'В центре комнаты находилась большая капсула, огороженная прозрачным стеклом.'
    
    show aly thinking at right with dissolve

    aly thinking "Что же это такое?"

    'Она осторожно вошла в помещение, пытаясь не привлекать внимания.'

    'На экранах она заметила сложные математические формулы:'

    aly normal "Это же формулы из физики и математики высокого уровня..."

    play sound "music/sounds/doorclosed2.mp3"

    'Вдруг дверь за ней закрылась, замок щёлкнул, и помещение наполнилось мягким голубым светом.'

    voice "Начинаем процедуру активации. Пожалуйста, оставайтесь на месте."

    aly scary "Эй! Кто здесь? Я случайно зашла! Откройте дверь, пожалуйста!"

    'Капсула в центре комнаты начала издавать гул, и панели на ней засветились. '

    'Крышка капсулы медленно поднялась, и из неё вышел андроид, внешне практически неотличимый от человека.'

    show android at left with dissolve

    android "Здравствуйте. Идентификационные данные отсутствуют. Запуск протокола безопасности."

    aly scary "Подождите! Я просто посетитель! Не знала, что сюда нельзя!"

    'Андроид начал приближаться к ней, его глаза светились холодным светом.'

    android "Пожалуйста, предъявите удостоверение личности для проверки."
    
    aly normal "У меня нет пропуска... Я была с Профессором, но он ушёл..."

    show android at left with move

    play sound "music/sounds/opendoor2.mp3"

    'В этот момент дверь внезапно открылась, и в комнату вбежали сотрудники безопасности вместе с Профессором.'

    show prof serious with dissolve

    prof alarm "Аля, быстрее за мной! Нам нужно добраться до панели управления, чтобы отключить протокол безопасности"

    show prof serious with move

    prof serious "Агх, автоматические системы заблокированны, придется делать всё в ручную"

    prof serious "Аля, помоги мне"
    
    aly normal "Да, сейчас!"


    jump start_hacking_game

    # Конец 6 главы


# Начало 7 главы
label Chapter_7:
    # НЕ ЗНАЮ НУЖНО ЛИ ТУТ МЕНЯТЬ ИЗОБРАЖЕНИЕ, Т.К. ПО СУТИ ЕГО НАДО ВСТАВЛЯТЬ КОГДА АЛЯ И ПРОФ ВЫХОДЯТ В КОРИДОР
    scene bg nightoffice with fade

    'На улице уже стемнело. Профессор проводил Алю до выхода.'

    show prof normal at right
    with dissolve 

    prof normal "Сегодня было много впечатлений. Надеюсь, ты не слишком испугалась." 
    show aly impressed with dissolve

    aly happy "Немного, но это было потрясающе! Я столько всего узнала. Теперь у меня гораздо более чёткое представление о разных профессиях в IT."

    prof normal "Это замечательно. Главное — выбрать путь, который будет приносить тебе удовольствие."

    aly confusion "Спасибо вам огромное за эту возможность. Теперь я чувствую себя гораздо увереннее."

    prof normal "Всегда пожалуйста. Если решишь связать свою жизнь с IT, мы будем рады видеть тебя в нашей команде."

    prof normal "Будут вопросы или захочешь глубже изучить что-то, обращайся."

    aly normal "Я подумаю над этим. Сегодня я поняла, насколько это интересно и многогранно."
    # Конец 7 ГЛАВЫ

    jump Epilogue
    
label Epilogue:

    scene black with fade
    
    n '''Спустя несколько месяцев Аля поступила в университет на факультет компьютерных наук.
    
    Она связалась с Профессором, и тот предложил ей стажировку в "Технограде". 

    Теперь она работала над реальными проектами, совершенствуя свои навыки.'''  

    aly normal '''Я так рада, что сделала этот шаг. Мир IT настолько разнообразен и увлекателен. 

    Я благодарна Профессору, Вальдемару, Францу и Виви за то, что помогли мне найти свой путь.

    Я готова к новым вызовам и открытиям. Мир IT — это именно то, что я искала.'''

    jump credits 
  
    return
 
init:
    transform txt_up:
        yalign 1.5
        linear 15.0 yalign -1.5

label credits:
    scene black with dissolve
    show text "Тимлид - Максим Ярославцев {p}{p} Сценарий - Павел Беляев {p}{p} Дизайн - Михаил Будущев {p}{p} Код - Григорий Марков, Никита Гришунин {p}{p} Всем спасибо! {p}{p} Конец" at txt_up
    pause 15
    stop music

    return
