import os

def get_jpgs(folder):
    path = os.path.join("images", folder)
    if os.path.exists(path):
        return [f"{path}/{f}" for f in sorted(os.listdir(path)) if f.lower().endswith(('.jpg', '.jpeg', '.webp'))]
    return []

def render_photos(folder, bg_class="bg-beige"):
    jpgs = get_jpgs(folder)
    if not jpgs:
        return f'<section class="gallery-wrapper {bg_class}"><div class="gallery-content"><p style="text-align:center; padding: 2vw; color: #a0978d; border: 1px dashed #ccc;">Здесь появится галерея фотографий «{folder}», когда вы добавите их в папку images/{folder}/</p></div></section>'
    
    html = f'<div class="gallery-wrapper {bg_class}"><div class="gallery-content">\n'
    for i, jpg in enumerate(jpgs):
        # Добавляем класс fade-in для анимации
        html += f'    <img src="{jpg}" class="fade-in" alt="photo" loading="lazy">\n'
    html += '</div></div>\n'
    return html

html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Презентация События</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');
        
        html {
            scroll-behavior: smooth; /* Плавный скролл для всей страницы */
        }

        body, html {
            margin: 0;
            padding: 0;
            background-color: #f2e9dc;
            font-family: 'Courier Prime', Courier, monospace;
            overflow-x: hidden;
        }

        .bg-beige { background-color: #f2e9dc; }
        .bg-blue { background-color: #1a1bd1; }

        /* 1 в 1 слайд из презентации, на всю ширину экрана */
        .slide {
            width: 100vw;
            aspect-ratio: 16 / 9;
            position: relative;
            container-type: inline-size;
            overflow: hidden;
            margin: 0;
            padding: 0;
        }

        .full-asset {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: contain;
            z-index: 1;
        }

        /* 1. КОНЦЕПЦИЯ - картинка на весь экран */
        #slide-concept {
            height: 100vh; /* Принудительно делаем первый экран по размеру окна, чтобы текст был по центру */
            background-image: url('assets/image1.jpg');
            background-size: cover;
            background-position: center;
        }

        /* 2. ДЕКОР */
        #slide-decor .text {
            position: absolute;
            left: 10%;
            top: 25%;
            color: #1a1bd1;
            font-size: 10cqi;
            font-weight: normal;
            z-index: 3;
            letter-spacing: -0.1cqi;
        }
        #slide-decor img.squiggle {
            position: absolute;
            left: 10%; /* Выравниваем с текстом */
            top: 70%; /* Сдвигаем СИЛЬНО ниже, так как из-за поворота она растет вверх */
            height: 38cqi; 
            width: auto;
            transform: rotate(-90deg);
            transform-origin: left top;
            z-index: 1; /* Опускаем слой ниже текста */
        }
        #slide-decor img.chair {
            position: absolute;
            right: 25%; /* Сдвигаем немного правее, так как оно станет больше */
            bottom: 5%;
            height: 75%; /* Делаем кресло значительно крупнее */
            z-index: 5;
        }
        #slide-decor img.wardrobe {
            position: absolute;
            right: 5%;
            bottom: 5%;
            height: 85%;
            z-index: 3;
        }

        /* 3. ДРЕСС-КОД */
        #slide-dresscode .text {
            position: absolute;
            left: 22%; /* Возвращаем на левую сторону, чуть правее скобки */
            top: 25%; /* Возвращаем на уровень скобки */
            color: #ffffff;
            font-size: 6.5cqi; /* Идеальный размер, чтобы поместиться между [ и ] */
            z-index: 2;
            line-height: 1.15;
        }

        /* 4. ПРОДАКШН */
        #slide-production .beam {
            position: absolute;
            left: 18%;
            top: 15%;
            width: 100%;
            height: 70%;
            background-color: #1a1bd1;
            clip-path: polygon(0 40%, 100% 0, 100% 100%, 0 60%);
            z-index: 1;
        }
        #slide-production .text {
            position: absolute;
            left: 32%; /* Сдвинули правее, чтобы не перекрывалось прожектором */
            top: 50%;
            transform: translateY(-50%);
            color: #ffffff;
            font-size: 5cqi;
            z-index: 4; /* Текст поверх всего */
        }
        #slide-production img.spotlight {
            position: absolute;
            left: 2%;
            top: 50%;
            transform: translateY(-50%);
            height: 60%;
            z-index: 3;
        }

        /* 5. ЛАЙН-АП */
        #slide-lineup .text {
            position: absolute;
            right: 15%;
            top: 50%;
            transform: translateY(-50%);
            color: #ffffff;
            font-size: 6cqi;
            z-index: 2;
        }

        /* 6. ТОРТ */
        #slide-cake .blue-box {
            position: absolute;
            right: 15%;
            top: 40%;
            background-color: #1a1bd1;
            padding: 1cqi 2cqi;
            z-index: 2;
        }
        #slide-cake .text {
            color: #ffffff;
            font-size: 5.5cqi;
        }

        /* Галереи фото */
        .gallery-wrapper {
            width: 100vw;
            display: flex;
            justify-content: center;
            margin: 0;
            padding: 0;
        }
        .gallery-content {
            width: 95%;
            margin: 2vw auto 4vw auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-auto-rows: 20vw; /* Фиксированная высота для строк сетки */
            gap: 1vw; /* Зазоры между фото как на скриншоте */
        }
        .gallery-content img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            margin: 0;
            padding: 0;
        }
        
        /* Интересная "блочная" сетка для 3 фото */
        .gallery-content img:nth-child(1) {
            grid-column: span 2;
            grid-row: span 2;
        }
        .gallery-content img:nth-child(2) {
            grid-column: span 1;
            grid-row: span 1;
        }
        .gallery-content img:nth-child(3) {
            grid-column: span 1;
            grid-row: span 1;
        }

        /* Анимации появления */
        .fade-in {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
"""

html_footer = """
<script>
document.addEventListener("DOMContentLoaded", () => {
    // Настраиваем IntersectionObserver для появления элементов при скролле
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Элемент начнет появляться, когда 15% его будет видно
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Добавляем класс visible
                entry.target.classList.add('visible');
                // Перестаем следить, чтобы анимация сработала один раз
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Ищем все элементы с классом fade-in
    const fadeElements = document.querySelectorAll('.fade-in');
    
    // Добавляем небольшую задержку (stagger) для элементов внутри одного контейнера
    let delay = 0;
    fadeElements.forEach((el, index) => {
        // Если элементы идут подряд (например, сетка фото), делаем их появление по очереди
        if (index > 0 && el.parentElement === fadeElements[index-1].parentElement) {
            delay += 150; // задержка 150ms между соседними фото
        } else {
            delay = 0;
        }
        el.style.transitionDelay = delay + 'ms';
        observer.observe(el);
    });
});
</script>
</body>
</html>
"""

# Assemble
html = html_template

# Concept
html += """
    <!-- Слайд 1: Concept -->
    <div id="slide-concept" class="slide">
    </div>
"""
html += render_photos('concept', 'bg-beige')

# Decor
html += """
    <!-- Слайд 2: Decor -->
    <div id="slide-decor" class="slide bg-beige">
        <div class="text">decor.</div>
        <img src="assets/image4.png" class="squiggle" alt="squiggle">
        <img src="assets/image3.png" class="chair" alt="chair">
        <img src="assets/image2.png" class="wardrobe" alt="wardrobe">
    </div>
"""
html += render_photos('decor', 'bg-beige')

# Dress-code
html += """
    <!-- Слайд 3: Dress-code -->
    <div id="slide-dresscode" class="slide bg-blue">
        <img src="assets/image5.png" class="full-asset" alt="dress-code silhouettes">
        <div class="text">dress-<br>code.</div>
    </div>
"""
html += render_photos('dresscode', 'bg-blue')

# Production
html += """
    <!-- Слайд 4: Digital Production -->
    <div id="slide-production" class="slide bg-beige">
        <div class="beam"></div>
        <div class="text">digital production.</div>
        <img src="assets/image6.png" class="spotlight" alt="spotlight">
    </div>
"""
html += render_photos('production', 'bg-beige')

# Lineup
html += """
    <!-- Слайд 5: Lineup -->
    <div id="slide-lineup" class="slide bg-blue">
        <img src="assets/image7.png" class="full-asset" alt="lineup silhouette">
        <div class="text">лайн-ап.</div>
    </div>
"""
html += render_photos('lineup', 'bg-blue')

# Cake
html += """
    <!-- Слайд 6: Cake -->
    <div id="slide-cake" class="slide bg-beige">
        <img src="assets/image8.png" class="full-asset" alt="wedding cake">
        <div class="blue-box">
            <span class="text">wedding cake.</span>
        </div>
    </div>
"""
html += render_photos('cake', 'bg-beige')

html += html_footer

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Site generated with true full width (100vw) slides!")
