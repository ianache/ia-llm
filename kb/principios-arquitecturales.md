[[_TOC_]]

# [Principios Generales de la Arquitectura](principaios-arquitecturales)

Los principios generales que gobiernan los diferentes aspectos de la arquitectura de la solución se encuentran resumidos en nueve (9) principios alineados con los pilares de la arquitectura de la solución (ver documento CLocator 2 Pilares de la Solución v1.0.docx adjunto). En la siguiente imagen, se resumen los Nueve Principios Arquitecturales:

![image](uploads/65c42d70c30bf6862510249e58263228/image.png)

## Principio 1: Soluciones Adaptables
> Colocar la definición detallada del principio arquitectural.

Las soluciones deben tener la capacidad de soportar escenarios de operación para contextos multi país, región / zona, monedas, empresa, canales y dispositivos.

### Lineamientos Arquitecturales

#### LA1.1 Flexibilidad en la incorporación de nuevos dispositivos (marcas y modelos)

- La arquitectura deberá permitir que se incorporen nuevos dispositivos (marcas y modelos) con nuevos protocolos y tramas de telemetría y control sin la necesidad de modificaciones a los componentes (microservicios) que procesan la telemetría.

- La incorporación de nuevos dispositivos (marcas y modelos) debe ser tratado a través de configuración sobre los componentes arquitecturales existentes de la arquitectura (se debe evitar crear nuevos componentes a la medida por cada protocolo) para procesamiento de telemetría.

- La solución se enfocará de forma primaria sobre una estrategia de configuración de nuevos protocolos (incluyendo facilidades para pruebas de los nuevos protocolos) en contraposición al desarrollo a la medida para cada protocolo reduciendo el time-to-market.

#### LA1.2 Adecuación a las preferencias de cada cliente (empresa)

- Los componentes **frontend** (Web, App Mobile) debe permitir que los clientes adecuen el Look & Feel a sus requerimientos institucionales para asegurar su identidad ante sus clientes finales.

- Los componentes **frontend** (Web, App Mobile) deben asegurar que los contenidos (textos, términos, etiquetas) se ajusten al contexto y requerimientos del cliente.

#### LA1.3 Adaptación a la región / zona de ubicación del cliente

- Toda la información que involucre fecha y hora debe ser tratada de acuerdo a la zona horaria del cliente.

- Todo el procesamiento que involucre información de fecha y hora debe operar tomando en consideración la zona horaria del cliente.

#### LA1.4 Integración con sistemas de terceros

- Se debe proporcionar mecanismos estándares para la integración con los sistemas de asociados de negocios en los países donde el Backoffice de Comsatel no soporte completamente la operación del negocio.

## Principio 2: Soluciones Abiertas

Las soluciones deben evitar fuerte acoplamiento (dependencia fuerte o de forma restrictiva) de un **único** proveedor, plataforma o tecnología subyacente que evite que estas puedan ser portadas o migradas hacia un nuevo contexto tecnológico (nuevo proveedor de servicios, plataforma equivalente o tecnología subyacentes equivalentes) 

### Lineamientos Arquitecturales

#### LA2.1 No locking con un único proveedor tecnológico

- Las decisiones sobre todo bloque de construcción de la solución deben ser formuladas asegurando que estos puedan ser trasladado hacia y operen sobre facilidades (servicios) de diferentes proveedores tecnológicos.

### LA2.2 Uso de estándares de industria

- Las decisiones deben basarse dando prioridad al uso de estándares tecnológicos de industria.

- Las decisiones arquitecturales se deben basr 

## Principio 3: Soluciones Escalables

Las soluciones deben tener la capacidad de adaptarse a escenarios de operación con demanda de recursos cambiantes en el tiempo, adaptándose a nuevas condiciones de operación preservando el cumplimiento de los SLAs/SLOs y funcionalidades comprometidas.

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí



#### LA3.1 DECLARACION DEL LINEAMIENTO

## Principio 4: Soluciones Omnicanales / Multicanales
> Colocar la definición detallada del principio arquitectural.

Las soluciones deben tener la capacidad de ser proporcionadas a los usuarios finales a través de canales diversos de acuerdo con requerimientos y estrategias de multi canalidad y/o omnicanalidad según corresponda a la estrategia se requiera en los diferentes escenarios de operación. 

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA4.1 DECLARACION DEL LINEAMIENTO

## Principio 5: Soluciones Interoperables
> Colocar la definición detallada del principio arquitectural.

Tomando en consideración que de acuerdo con [HIMSS](https://www.himss.org/resources/interoperability-healthcare#Part1) la interoperabilidad es “the ability of different information systems, devices and applications (systems) to access, exchange, integrate and cooperatively use data in a coordinated manner, within and across organizational, regional and national boundaries, to provide timely and seamless portability of information and optimize the health of individuals and populations globally.”; las soluciones deben tener la capacidad de interactuar tanto al interno de COMSATEL como con soluciones externas basadas en uso de estándares de facto. La interoperabilidad debe darse a diferentes niveles (fundacional, estructural y semántico).

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA5.1 DECLARACION DEL LINEAMIENTO

## Principio 6: Soluciones Fiables
> Fiabilidad del software "...is the probability of failure-free operation of a computer program for a specified period in a specified environment. Reliability is a customer-oriented view of software quality" [CMU](https://users.ece.cmu.edu/~koopman/des_s99/sw_reliability/#:~:text=Software%20Reliability%20is%20the%20probability,time%20in%20a%20specified%20environment.)

Las soluciones deben tener la capacidad de ofrecer servicios conforme al SLA anual (disponibilidad) por COMSATEL; asegurando alta disponibilidad (evitar únicos puntos de fallas) y continuidad de la operación de los clientes internos y externos.

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA6.1 DECLARACION DEL LINEAMIENTO

## Principio 7: Soluciones Seguras
> Colocar la definición detallada del principio arquitectural.

Las soluciones deben tener la capacidad de proporcionar un contexto seguro para las operaciones de negocios soportadas, acuerdo con la normativas, políticas y estándares vigentes aplicables tanto para nuestros clientes externos como los internos.

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA7.1 DECLARACION DEL LINEAMIENTO

## Principio 8: Soluciones Personalizables
> Colocar la definición detallada del principio arquitectural.

Las soluciones deben tener la capacidad de ser personalizadas (look and feel, etiquetas, idioma, parametría, entre otros) de acuerdo con las necesidades y características de los clientes tanto internos como externos.

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA8.1 DECLARACION DEL LINEAMIENTO

## Principio 9: Soluciones Gestionables
> Colocar la definición detallada del principio arquitectural.

Al nivel de la plataforma base y de la solución se debe asegurar la capacidad de poder monitorear diferentes parámetros que aseguren un nivel adecuado de gestión de la operación conforme con los SLAs / SLOs comprometidos. 

Las capacidades de monitoreo y observabilidad deben asegurar visibilidad y emisión de alertas ante comportamientos de la plataforma y solución no acordes con SLAs / SLOs comprometidos.

### Lineamientos Arquitecturales

> Colocar los lineamientos aquí

#### LA9.1 Todos los microservicios deben exponer métricas basadas en protocolo Prometheus

- Los microservicios DEBEN exponer las métricas de su comportamiento a través del protocolo de exposición de prometheus.

- La plataforma DEBE tener configurado los niveles de alertas como mínimo para casos de consumo de CPU y Memoria que excedan un umbral del `80%` del uso del recurso.

- Las alertas DEBEN ser notificadas en línea a responsables del 

