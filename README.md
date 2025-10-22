ocker compose up -d –build (crea contenedores usando mi dockerfile)
2.	docker-compose run --rm airflow-webserver airflow db init (Esto lo hago ya que para poder lanzar mi scheduler debe estar la base de datos arriba antes)
3.	docker-compose up -d (ahora si subo todos los contenedores)
4.	Genero usuario para logearme en Airflow
docker-compose run --rm airflow-webserver airflow users create \
--username admin \
--firstname Admin \
--lastname User \
--role Admin \
--email admin@example.com \
--password admin

