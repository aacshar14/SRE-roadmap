# SRE Workshop: Fundamentos y Práctica

Este workshop está diseñado para introducirte en los conceptos clave de Site Reliability Engineering (SRE), con un enfoque especial en la medición de confiabilidad a través de SLIs y SLOs.

## Parte 1: Las 5 Golden Signals (Señales de Oro)

Para tener una observabilidad efectiva, Google recomienda enfocarse en estas señales clave. Hemos añadido "Disponibilidad" como la quinta señal esencial.

1.  **Latencia (Latency):** El tiempo que tarda una solicitud en ser atendida.
    *   *Importante:* Distingue entre latencia de éxitos y de errores. Una respuesta de error 500 puede ser muy rápida, sesgando tus métricas.
2.  **Tráfico (Traffic):** La demanda que recibe tu sistema.
    *   *Ejemplo:* Peticiones HTTP por segundo, o transacciones de base de datos.
3.  **Errores (Errors):** La tasa de solicitudes que fallan.
    *   *Tipos:* Explícitos (HTTP 500), implícitos (HTTP 200 pero con contenido vacío o incorrecto), o por política (respuesta > 1 seg).
4.  **Saturación (Saturation):** Qué tan "lleno" está tu servicio.
    *   *Métrica:* Uso de CPU, memoria, I/O. Mide la fracción "ocupada" de tu recurso más limitado.
5.  **Disponibilidad (Availability):** El porcentaje de tiempo que el sistema es utilizable.
    *   *Relación:* A menudo se define en función de las tasas de éxito de las otras señales.

---

## Parte 2: Los 10 Pasos Fundamentales de SRE

1.  **Fundamentos y Cultura:** SRE no es solo tecnología. Se basa en una cultura "blameless" (sin culpa) y seguridad psicológica para reportar incidentes.
2.  **SLIs (Service Level Indicators):** ¿Qué métrica precisa nos dice si el usuario está feliz? (ej. latencia del 99% de las peticiones).
3.  **SLOs (Service Level Objectives):** El objetivo numérico para ese SLI (ej. 99.9% de los requests deben ser exitosos).
4.  **Error Budgets (Presupuesto de Error):** 100% - SLO. Es el margen que tenemos para fallar. Si se agota, congelamos lanzamientos para estabilizar.
5.  **Toil Reduction (Reducción de Trabajo Penoso):** Automatizar tareas manuales, repetitivas y sin valor estratégico que crecen línealmente con el servicio.
6.  **Monitoreo y Observabilidad:** Implementar las 5 Golden Signals. Pasar de "¿está arriba el servidor?" a "¿funciona el servicio para el usuario?".
7.  **Respuesta a Incidentes:** Tener roles claros (Comandante de Incidente, Comunicación, Ops) y procedimientos definidos antes de que ocurra el fuego.
8.  **Postmortems:** Análisis detallado tras un incidente. El objetivo no es buscar culpables, sino arreglar el proceso o sistema que permitió el fallo.
9.  **Capacity Planning:** Predecir crecimiento futuro (orgánico o por lanzamientos) para asegurar recursos suficientes antes de la saturación.
10. **Chaos Engineering & Resiliencia:** Romper cosas a propósito en entornos controlados para entrenar al equipo y validar que los sistemas de recuperación funcionan.

---

## Parte 3: Deep Dive - SLOs y SLIs

El núcleo de SRE es tomar decisiones basadas en datos, y para eso necesitamos definir qué significa "confiabilidad".

### Definiciones

*   **SLI (Indicador):** Medida cuantitativa de algún aspecto del nivel de servicio.
    *   `SLI = (Eventos Buenos / Eventos Totales) * 100`
*   **SLO (Objetivo):** Valor objetivo o rango de valores para un nivel de servicio medido por un SLI.
    *   `SLI >= SLO`

### Ejemplo Práctico: Servicio de Login

Imagina un servicio de autenticación.

**Paso 1: Elegir el SLI**
No nos importa si la CPU está al 10% o al 90% si el usuario entra rápido.
*   *Métrica:* Disponibilidad (Latencia + Correctitud).
*   *Definición:* La proporción de peticiones válidas a `/login` que responden con HTTP 200 y en menos de 500ms.

**Paso 2: Definir el SLO**
¿Necesitamos 100%? Probablemente no, y es muy caro.
*   *Objetivo:* 99.9% mensual.

**Paso 3: Calcular el Error Budget**
En una ventana de 30 días (aprox 43,200 minutos), un 99.9% de disponibilidad significa:
*   **Tiempo permitido de caída:** 43.2 minutos (`43,200 * (1 - 0.999)`).

### Ejercicio de Taller

*Escenario:* Recibes 1,000,000 de peticiones a la semana. Tu SLO es 99.95%.

1.  **¿Cuántas peticiones pueden fallar?**
    *   Total: 1,000,000
    *   Permitido fallar: 0.05% -> `0.0005 * 1,000,000` = **500 peticiones**.

2.  **Situación:** Un deploy el martes causó 200 errores 500 durante 5 minutos.
    *   Consumo del presupuesto: 200 / 500 = 40%.
    *   *Decisión:* Todavía tienes 60% del presupuesto. Puedes seguir lanzando features, pero con cuidado.
