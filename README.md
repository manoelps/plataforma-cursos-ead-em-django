# Projeto Django - Cursos EaD FAESA

Este projeto é uma página de apresentação dos cursos EaD da FAESA, utilizando o framework Django.

## 🚀 Tecnologias utilizadas

- Python 3.10+
- Django 4.x
- HTML5 + CSS3 (com Flexbox)
- Estrutura de arquivos estáticos e templates

---

## 📦 Estrutura de diretórios

```
faesa/
├── cursos/
│   ├── templates/
│   │   └── cursos/
│   │       └── index.html
│   ├── static/
│   │   └── cursos/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── images/
│   │           ├── logo-faesa.png
│   │           ├── analise.png
│   │           ├── redes.png
│   │           └── sistemas.png
│   └── views.py
├── faesa/
│   └── settings.py
└── manage.py
```

---

## ⚙️ Passos para executar o projeto

1. **Clone o repositório ou extraia o ZIP**

Se estiver com o projeto zipado:

```bash
unzip plataforma-cursos-ead.zip
cd plataforma-cursos-ead
```

2. **Crie e ative um ambiente virtual (recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale o Django:**

```bash
pip install django
```

4. **Execute o servidor:**

```bash
python manage.py runserver
```

5. **Acesse no navegador:**

```
http://127.0.0.1:8000/
```

ou

```
http://localhost:8000/
```
