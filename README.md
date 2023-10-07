### Desafío:
Necesitamos un proceso de registración de los leads a procesar. Estos leads, son personas
cursando materias de una carrera. Lo que se necesita registrar es la persona y las N materias
que cursa en N carreras, donde N va de 0 a X.
Para ello se pide realizar:

#### * Front (BONUS EXTRA) – NO ES OBLIGATORIO EL FRONT
Interfaz con validación de los campos a ingresar (Nombre completo, email, dirección, teléfono,
materia, tiempo de cursado, carrera, año de inscripción, número de veces cursada la materia, y
otros que se consideren necesario). Una vez cargado el lead de forma satisfactoria, tiene que
mostrar una confirmación con el id del registro para trazabilidad.
NOTA: Si no se ejecuta el bono, la carga del LEAD puede ser realizada previamente a mano. O
pasando el String directamente a la API. (ver como ingresa en la sección BACK)

#### * Back (NECESARIO)
Api restful que procese la carga, y disponibilice el resultado de los leads cargados paginados
en otro endpoint, mas un get por id de registro. El mismo debe ser realizado en Python con el
framework de FastAPI.

#### * Infra (NECESARIO)
Dockerizar el frontend (ej el caso de tomar el Bonus) y el backend y componer (docker
compose) las soluciones. Utilizar un motor relacional (postgres preferentemente) para la
persistencia.

#### * Codigo (NECESARIO)
Disponibilizar la solución en un repositorio git público, puede ser github. Documentar la solución
tanto de manera funcional como técnica en el readme del repositorio.
Una vez finalizado el challenge, solo se tiene que presentar la url al repositorio público por
email con un tag de la rama principal donde queden congelados los cambios. 
