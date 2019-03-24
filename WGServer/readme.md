!---------------------------------- 

! WGServer запуск проверки веток 

!----------------------------------

необходимо установить: Flask, paramiko

1. Здесь уникальны хосты а не пользователи (по админской практике юзеры на машинах могут быть одинаковые)
2. Т.к. для меня не понятные json запросы в задании, точнее недостаточно данных, я отталкиваюсь от:
	
	2.1 добавить хост

		POST 
			curl "http://localhost:8880/warapig/0.1/host&key=Art0fWar" 
			-d "{"user": "root", "hostname": "10.10.10.10"}"
	2.2 добавить массив хостов 

		POST 
			curl "http://localhost:8880/warapig/0.1/hosts&key=Art0fWar" 
			-d "{hosts: [
				{"user": "root", "hostname": "10.10.10.10"}
				, {"user": "root", "hostname": "10.10.10.11"}
				]}"

	дополнительные поля которые могут быть указаны
			"username": "Vasja Pupkin"
			
	в паре
			"auth_type": "psw", "password": "DieMyDarling" 
		или
			"auth_type": "key", "key": "asasdasdasdasd65asd765asd67as5d6"
	
	2.3 получить инфу по хосту

		GET curl -XPOST -H 'Content-Type: application/json' 
		"http://localhost:8880/warapig/0.1/host/10.10.10.10&key=Art0fWar"

	полный ответ

			{"username": "Vasja Pupkin", 
			 "user": "root", 
			 "auth_type": "password", 
			 "host": "10.10.10.150", 
			 "active": true, 
			 "git": {
				"branch": "master", "revision": "1asdasd"}
			 "svn": {
				"branch": "https://svnserver/project", "revision": "1"}
			}

	если нет подключения к хосту то git и svn будут отсутсвовать

	2.4 получить информацию по хостам

		GET  "http://localhost:8880/warapig/0.1/hosts&key=Art0fWar"
		
	ответ

			{"hosts": [
				{"username": "Vasja Pupkin", "user": "root", "auth_type": "password", "host": "10.10.10.10", 
			 	 "active": false},  
				{"username": "NoName", "user": "root", "auth_type": "password", "host": "10.10.10.11", 
			 	 "active": false}
			]}
