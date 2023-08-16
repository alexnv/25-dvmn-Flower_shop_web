# ssh
Путь к файлу конфигурации .ssh/config
Добавить записи
```
Host bakecake
    HostName 81.163.27.248
    User root
    ForwardAgent yes
```

Заходим на сервак и создаем ппользователя
useradd curator -m -s /bin/bash 
пепреходим в корень
cd ~
и по ссылке ниже выпполняем команды
[Про руннер](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)


Затем выбираем docker image в меню Actions нашего репозитория
Breadcrumbs22-dvmn-BakeCake/.github/workflows / docker-image.yml     in master
# Исправляем 


    runs-on: self-hosted

    
    steps:
    - uses: actions/checkout@v3
    - name: build and run
       env:
          DEBUG: True
          SECRET_KEY: 12345
          ALLOWED_HOSTS: localhost
       run: docker compose up -d --build



т.к. на серваке не  установлен докер в соседней консоли от рута  пишем

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

[и далее ппо шагам](https://docs.docker.com/engine/install/debian/) устанавливаем докер


затем

usermod -a -G docker curator



# [В ппомощь статья на Хабре](https://habr.com/ru/articles/711278/)
