
 export interface Segpara{
    aplicacion?:string,
    parametro?:string,
    descripcion?:string,
    status?:string
 }
 
 export interface Segpaag{
    aplicacion?:string,
    nom_aplicacion?:string,
    parametro?:string,
    nom_parametro?:string,
    valor?:string,
    status?:string,
    nom_status?:string
}

export interface Natur{
    naturaleza?:string,
    nombre?:string,
    cargo?:string,
    creado_por?:string,
    fecha_creado?:string,
    hora_creado?:string,
    status?:string,
    modificado_por?:string,
    fecha_status?:string,
    hora_status?:string,
    nom_cargo?:string,
    nom_status?:string
}

export interface Scggcta {
    tipo_cuenta?:string,
    descripcion?:string,
    uso?:string,
    nom_uso?:string,
    status?:string,
    nom_status?:string,
}

export interface Scgsgcta {
    tipo_cuenta?:string,
    grupo_cuenta?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string
}

export interface Scgcata {
    cuenta?:string,
    descripcion?:string,
    naturaleza?:string,
    nom_naturaleza?:string,
    nivel_cuenta?:string,
    nom_nivel?:string,
    tipo_cuenta?:string,
    nom_tipo?:string,
    grupo_cuenta?:string,
    nom_grupo?:string,
    recibe?:string,
    aux_interno?:string,
    aux_externo?:string,
    status?:string,
    nom_status?:string
}

export interface Scgcodi {
    nivel_cuenta?:string,
    descripcion?:string,
    inicio_cuenta?:string,
    final_cuenta?:string,
    no_posiciones?:string,
    status?:string,
    nom_status?:string
}

export interface Scgterc {
    tercero?:string,
    descripcion?:string,
    tipo_interno?:string,
    no_cedula?:string,
    no_ruc?:string,
    digito_verificador?:string,
    no_placa?:string,
    status?:string,
    nom_status?:string
}

export interface Scgsist {
    sistema?:string,
    descripcion?:string,
    uso?:string,
    secuencial?:string,
    status?:string,
    nom_status?:string
}

export interface Scgtitr {
    sistema?:string,
    transaccion?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string
}

export interface Scgtran {
    sistema?:string,
    transaccion?:string,
    libro?:string,
    db_cr?:string,
    status?:string,
    nom_status?:string
}
 
export interface Seggere {
    compania?:string,
    gerencia?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string
}

export interface Segdept {
    compania?:string,
    gerencia?:string,
    departamento?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string
}

export interface Scgdept {
    compania?:string,
    gerencia?:string,
    departamento?:string,
    tipo_aplica?:string,
    clase?:string,
    subclase?:string,
    status?:string,
}

export interface Scgclas {
    tipo_aplica?:string,
    clase?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string, 
}

export interface Scgscla {
    tipo_aplica?:string,
    clase?:string,
    subclase?:string,
    descripcion?:string,
    status?:string,
    nom_status?:string,   
}

export interface Scgtapl {
    tipo_aplica?: string,
    descripcion?: string,
    uso?: string,
    status?: string,
    nom_status?: string
}