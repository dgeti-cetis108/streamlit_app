import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Registro de Estudiantes",
    page_icon="🎓",
    layout="wide"
)

# Inicializar session_state
if 'seccion' not in st.session_state:
    st.session_state.seccion = 1

if 'datos' not in st.session_state:
    st.session_state.datos = {}

# Función para avanzar sección
def siguiente_seccion():
    st.session_state.seccion += 1

# Función para retroceder sección
def anterior_seccion():
    st.session_state.seccion -= 1

# Función para reiniciar
def reiniciar():
    st.session_state.seccion = 1
    st.session_state.datos = {}

# Título principal
st.title("📝 Formulario de Registro de Estudiantes")
st.markdown("**Formulario progresivo paso a paso**")

# Barra de progreso
progreso = st.session_state.seccion / 5
st.progress(progreso)
st.markdown(f"**Sección {st.session_state.seccion} de 5**")
st.markdown("---")

# SECCIÓN 1: Información Personal
if st.session_state.seccion == 1:
    st.subheader("👤 Sección 1: Información Personal")
    
    nombres = st.text_input(
        "¿Cuál es tu nombre(s)? *",
        value=st.session_state.datos.get('nombres', ''),
        placeholder="Ej: Juan Carlos"
    )
    
    apellidos = st.text_input(
        "¿Cuáles son tus apellidos? *",
        value=st.session_state.datos.get('apellidos', ''),
        placeholder="Ej: García López"
    )
    
    genero = st.radio(
        "¿Cuál es tu género? *",
        options=["Masculino", "Femenino", "Otro", "Prefiero no decir"],
        index=["Masculino", "Femenino", "Otro", "Prefiero no decir"].index(
            st.session_state.datos.get('genero', 'Masculino')
        ),
        horizontal=True
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Siguiente ➡️", use_container_width=True, type="primary"):
            if nombres.strip() and apellidos.strip():
                st.session_state.datos['nombres'] = nombres
                st.session_state.datos['apellidos'] = apellidos
                st.session_state.datos['genero'] = genero
                siguiente_seccion()
                st.rerun()
            else:
                st.error("Por favor completa todos los campos obligatorios")

# SECCIÓN 2: Escuela y Semestre
elif st.session_state.seccion == 2:
    st.subheader("🏫 Sección 2: Información de tu Institución")
    
    escuela = st.selectbox(
        "¿En qué escuela o facultad estudias? *",
        options=[
            "Selecciona una opción",
            "Ingeniería",
            "Ciencias",
            "Medicina",
            "Derecho",
            "Arquitectura",
            "Administración",
            "Artes",
            "Humanidades"
        ],
        index=0 if 'escuela' not in st.session_state.datos else [
            "Selecciona una opción",
            "Ingeniería",
            "Ciencias",
            "Medicina",
            "Derecho",
            "Arquitectura",
            "Administración",
            "Artes",
            "Humanidades"
        ].index(st.session_state.datos.get('escuela'))
    )
    
    semestre = st.number_input(
        "¿En qué semestre te encuentras? *",
        min_value=1,
        max_value=12,
        value=st.session_state.datos.get('semestre', 1),
        step=1
    )
    
    turno = st.select_slider(
        "¿En qué turno estudias? *",
        options=["Matutino", "Vespertino", "Nocturno"],
        value=st.session_state.datos.get('turno', 'Matutino')
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button("⬅️ Anterior", use_container_width=True):
            anterior_seccion()
            st.rerun()
    with col3:
        if st.button("Siguiente ➡️", use_container_width=True, type="primary"):
            if escuela != "Selecciona una opción":
                st.session_state.datos['escuela'] = escuela
                st.session_state.datos['semestre'] = semestre
                st.session_state.datos['turno'] = turno
                siguiente_seccion()
                st.rerun()
            else:
                st.error("Por favor selecciona una escuela")

# SECCIÓN 3: Grupo y Materias
elif st.session_state.seccion == 3:
    st.subheader("📚 Sección 3: Grupo y Materias")
    
    grupo = st.text_input(
        "¿Cuál es tu grupo? *",
        value=st.session_state.datos.get('grupo', ''),
        placeholder="Ej: A, B, 101",
        max_chars=10
    )
    
    materias = st.multiselect(
        "¿Qué materias estás cursando actualmente? *",
        options=[
            "Matemáticas",
            "Física",
            "Química",
            "Programación",
            "Bases de Datos",
            "Redes",
            "Algoritmos",
            "Cálculo",
            "Álgebra",
            "Estadística"
        ],
        default=st.session_state.datos.get('materias', []),
        help="Puedes seleccionar una o más materias"
    )
    
    st.info("💡 Selecciona todas las materias que apliquen")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button("⬅️ Anterior", use_container_width=True):
            anterior_seccion()
            st.rerun()
    with col3:
        if st.button("Siguiente ➡️", use_container_width=True, type="primary"):
            if grupo.strip() and materias:
                st.session_state.datos['grupo'] = grupo
                st.session_state.datos['materias'] = materias
                siguiente_seccion()
                st.rerun()
            else:
                st.error("Por favor completa el grupo y selecciona al menos una materia")

# SECCIÓN 4: Información Adicional
elif st.session_state.seccion == 4:
    st.subheader("📧 Sección 4: Información de Contacto (Opcional)")
    
    email = st.text_input(
        "Correo Electrónico",
        value=st.session_state.datos.get('email', ''),
        placeholder="ejemplo@escuela.edu.mx"
    )
    
    fecha_nacimiento = st.date_input(
        "Fecha de Nacimiento",
        value=st.session_state.datos.get('fecha_nacimiento'),
        min_value=datetime(1990, 1, 1),
        max_value=datetime.now()
    )
    
    comentarios = st.text_area(
        "Comentarios Adicionales",
        value=st.session_state.datos.get('comentarios', ''),
        placeholder="Escribe aquí cualquier información adicional...",
        max_chars=500,
        height=150
    )
    
    st.info("💡 Estos campos son opcionales pero nos ayudan a conocerte mejor")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button("⬅️ Anterior", use_container_width=True):
            anterior_seccion()
            st.rerun()
    with col3:
        if st.button("Siguiente ➡️", use_container_width=True, type="primary"):
            st.session_state.datos['email'] = email
            st.session_state.datos['fecha_nacimiento'] = fecha_nacimiento
            st.session_state.datos['comentarios'] = comentarios
            siguiente_seccion()
            st.rerun()

# SECCIÓN 5: Confirmación y Envío
elif st.session_state.seccion == 5:
    st.subheader("✅ Sección 5: Confirmación de Datos")
    
    st.success("¡Casi terminamos! Revisa tu información antes de enviar")
    
    # Mostrar resumen
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Información Personal")
        st.write(f"**Nombre completo:** {st.session_state.datos.get('nombres')} {st.session_state.datos.get('apellidos')}")
        st.write(f"**Género:** {st.session_state.datos.get('genero')}")
        
        st.markdown("### 🏫 Información Académica")
        st.write(f"**Escuela:** {st.session_state.datos.get('escuela')}")
        st.write(f"**Semestre:** {st.session_state.datos.get('semestre')}")
        st.write(f"**Grupo:** {st.session_state.datos.get('grupo')}")
        st.write(f"**Turno:** {st.session_state.datos.get('turno')}")
    
    with col2:
        st.markdown("### 📚 Materias")
        materias = st.session_state.datos.get('materias', [])
        for materia in materias:
            st.write(f"• {materia}")
        
        st.markdown("### 📧 Contacto")
        if st.session_state.datos.get('email'):
            st.write(f"**Email:** {st.session_state.datos.get('email')}")
        if st.session_state.datos.get('fecha_nacimiento'):
            st.write(f"**Fecha de nacimiento:** {st.session_state.datos.get('fecha_nacimiento').strftime('%d/%m/%Y')}")
    
    if st.session_state.datos.get('comentarios'):
        st.markdown("### 💬 Comentarios")
        st.info(st.session_state.datos.get('comentarios'))
    
    st.markdown("---")
    
    acepta_terminos = st.checkbox("Acepto los términos y condiciones *")
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col2:
        if st.button("⬅️ Anterior", use_container_width=True):
            anterior_seccion()
            st.rerun()
    
    with col3:
        if st.button("✅ Enviar", use_container_width=True, type="primary"):
            if acepta_terminos:
                st.balloons()
                st.success("🎉 ¡Registro completado exitosamente!")
                st.info("Tus datos han sido guardados correctamente")
                
                # Aquí podrías guardar en base de datos
                # guardar_en_db(st.session_state.datos)
                
                if st.button("📝 Nuevo Registro", use_container_width=True):
                    reiniciar()
                    st.rerun()
            else:
                st.error("Debes aceptar los términos y condiciones para continuar")
    
    with col4:
        if st.button("🔄 Reiniciar", use_container_width=True):
            reiniciar()
            st.rerun()

# Footer
st.markdown("---")
st.caption("📌 Los campos marcados con * son obligatorios")