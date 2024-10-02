# Используем официальный образ Nginx
FROM nginx:latest

# Устанавливаем рабочую директорию
WORKDIR /etc/nginx

# Копируем конфигурационный файл Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Создаем директории для конфигурационных файлов сайтов
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled

# Копируем конфигурационные файлы для сайтов
COPY nginx/sites-available /etc/nginx/sites-available

# Создаем символические ссылки для сайтов
RUN ln -s /etc/nginx/sites-available/bisband /etc/nginx/sites-enabled/bisband

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
