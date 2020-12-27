# LAB 4

## Хід роботи

1) Ознайомився з документацією докер.
2) Виконав команди, перенаправив вивід 
цих команд у файл my_work.log та закомітив
його до репозиторію.

        docker -v>>my_work.log
        docker -h>>my_work.log
        docker run docker/whalesay cowsay Docker is fun>>my_work.log
3) Ознайомився з документацією.
4) Використав команду щоб завантажити 
базовий імедж з репозиторію , 
створив Dockerfile та закомітив його  : 
        
         sudo docker pull python:3.8-slim
         sudo docker images
         sudo docker inspect python:3.8-slim
5) Створив реаозиторій на Docker Hub 
6) Виконав білд (build) Docker імеджа та завантажив 
його до репозиторію.
[Репозиторій](https://hub.docker.com/r/cieldidux/lab4)
[Імедж](https://hub.docker.com/layers/cieldidux/lab4/django/images/sha256-9dc4f78ff2a6e628444c57bf91df61453369499c8a279d954dafa68cfdb581f9?context=explore)
        
          sudo docker build -t cieldidux/lab4:django .
          sudo docker images
          sudo docker push cieldidux/lab4:django
7) Запустив сайт (все працює)
    
          sudo docker run -it --rm -p 8000:8000 cieldidux/lab4:django 
8) Cтворив Dockerfile.monitor. Виконав білд (build) Docker імеджа 
 з моніторингом та завантажив його до репозиторію.
[Імедж](https://hub.docker.com/layers/cieldidux/lab4/monitoring/images/sha256-9dc4f78ff2a6e628444c57bf91df61453369499c8a279d954dafa68cfdb581f9?context=explore)

          sudo docker build -t cieldidux/lab4:monitoring --file Dockerfile.monitor .
          sudo docker images
          sudo docker push cieldidux/lab4:monitoring
    Запустив обидва імеджі.
    
          sudo docker run -it --rm -p 8000:8000 cieldidux/lab4:django
          sudo docker run --net=host --rm -it cieldidux/lab4:monitoring
9) Для того щоб отримати логи я використав  docker exec

          sudo docker ps
    Знайшов необхідний ID (8787641e0fe7) 
    
          sudo docker exec -it 8787641e0fe7 /bin/bash   
          cat server.log
Частина з виведедених даних

		INFO 2020-11-24 17:59:14,697 root : Ключ: client_info, Значення: python-requests/2.22.0
		INFO 2020-11-24 18:00:14,723 root : Сервер доступний. Час на сервері: 24/11/2020 16:00:14
		INFO 2020-11-24 18:00:14,724 root : Запитувана сторінка: : http://localhost:8000/health/
		INFO 2020-11-24 18:00:14,724 root : Відповідь сервера містить наступні поля:
		INFO 2020-11-24 18:00:14,724 root : Ключ: date, Значення: 24/11/2020 16:00:14
		INFO 2020-11-24 18:00:14,724 root : Ключ: current_page, Значення: http://localhost:8000/health/
		INFO 2020-11-24 18:00:14,724 root : Ключ: server_info, Значення: ['Linux', 'ciel-VirtualBox', '5.4.0-52-generic', '#57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020', 'x86_64']
		INFO 2020-11-24 18:00:14,724 root : Ключ: client_info, Значення: python-requests/2.22.0
		INFO 2020-11-24 18:01:14,737 root : Сервер доступний. Час на сервері: 24/11/2020 16:01:14
		INFO 2020-11-24 18:01:14,738 root : Запитувана сторінка: : http://localhost:8000/health/
		INFO 2020-11-24 18:01:14,738 root : Відповідь сервера містить наступні поля:
		INFO 2020-11-24 18:01:14,738 root : Ключ: date, Значення: 24/11/2020 16:01:14
		INFO 2020-11-24 18:01:14,738 root : Ключ: current_page, Значення: http://localhost:8000/health/
