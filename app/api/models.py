"""Pydantic models for Balanz API responses."""
from typing import Optional, List
from pydantic import BaseModel, Field


class InitResponse(BaseModel):
    """Response from /auth/init endpoint."""
    tipoAutenticacion: int
    user: str
    URLAuth: str
    nonce: str


class LoginResponse(BaseModel):
    """Response from /auth/login endpoint."""
    idAplicacion: int
    idProductor: Optional[str] = None
    idPersona: str
    Nombre: str
    idSesion: str
    AccessToken: str
    Avatar: str
    email: str
    TipoDocumento: str
    Documento: str
    TelefonoFijo: str
    TelefonoMovil: str
    tieneC4D: str
    CaraRegistrada: Optional[str] = None
    CUIL: str
    UltimoLogin: str
    EsMenor: str
    user: str


class TenenciaDetalle(BaseModel):
    """Detailed holdings by currency."""
    orden: int
    idMoneda: int
    Moneda: str
    ValorActual: float
    VariacionPorcentual: float
    VariacionAbsoluta: float
    Rendimiento: float
    NoRealizado: float
    Cantidad: int
    idMonedaValuacion: int


class TenenciaAgrupada(BaseModel):
    """Holdings grouped by asset type."""
    valorTotal: float
    Cantidad: int
    Tipo: str
    detalle: List[TenenciaDetalle]
    idTipoInstrumento: int
    Color: str


class Tenencia(BaseModel):
    """Individual position details."""
    Tipo: str
    Ticker: str
    idMoneda: int
    Grilla: int
    Moneda: str
    Descripcion: str
    Cantidad: float
    Disponible: float
    Garantias: float
    Precio: float
    PPP: float
    ValorInicial: float
    ValorActual: float
    ValorActualPesos: float
    PorcTenencia: float
    NoRealizado: float
    PorcRendimiento: float
    TNA: str
    Variacion: str
    PrecioAnterior: float
    FechaUltimoOperado: str
    DiasPromedioTenencia: float
    panel: int
    BaseTicker: Optional[str] = None


class Liquidez(BaseModel):
    """Cash/liquidity by currency."""
    idMoneda: int
    Moneda: str
    Simbolo: str
    DInm: float
    DOInm: float
    FInm: str
    D24: float
    DO24: float
    F24: str
    D48: float
    DO48: float
    F48: str
    D72: float
    DO72: float
    F72: str
    DFut: float
    DOFut: float
    Cotizacion: float
    DO: float


class TenenciaActual(BaseModel):
    """Current portfolio summary."""
    TotalPesos: float
    Total: float
    TotalAnterior: float
    Movimientos: float
    Instrumentos: float
    InstrumentosPesos: float
    InstrumentosDolares: float
    Monedas: float
    SimboloMoneda: str
    Disponible: float
    VariacionAbs: float
    VariacionRel: float
    TextoCotizacionDolar: str
    CotizacionMEP: float
    CotizacionCCL: float


class EstadoDeCuentaResponse(BaseModel):
    """Response from /estadodecuenta endpoint."""
    tenenciaAgrupada: List[TenenciaAgrupada]
    tenencia: List[Tenencia]
    liquidez: List[Liquidez]
    tenenciaActual: List[TenenciaActual]


class ResumenItem(BaseModel):
    """Summary item from performance report."""
    id: int
    Nombre: str
    Rango: float
    Field1M: float = Field(alias="1M")
    Field3M: float = Field(alias="3M")
    Field6M: float = Field(alias="6M")
    YTD: float
    Field12M: float = Field(alias="12M")

    class Config:
        populate_by_name = True


class Rendimiento(BaseModel):
    """Daily performance record."""
    Fecha: str
    Rendimiento: float
    RendimientoAbs: float


class TenenciaHistorica(BaseModel):
    """Historical portfolio value."""
    Fecha: str
    Tenencia: float
    Dolares: float
    Pesos: float
    Bonos: float
    FCI: float
    Acciones: float
    Monedas: float
    MonedasPesos: float
    MonedasDolares: float
    Opciones: float


class Evento(BaseModel):
    """Transaction/event record."""
    date: str
    type: str
    backgroundColor: str
    graph: str
    text: str
    description: str


class EvolucionDeCarteraResponse(BaseModel):
    """Response from /evoluciondecartera endpoint."""
    resumen: List[ResumenItem]
    rendimiento: List[Rendimiento]
    tenencia: List[TenenciaHistorica]
    eventos: List[Evento]


class BonoDetalle(BaseModel):
    """Bond details."""
    descripcionbono: str
    codigoespeciebono: str
    tenencia: float
    precio: float
    tir: str
    tna: str
    spread: str
    duration: float
    int_corr: float
    prox_pago: str
    vto: str
    amort: str
    frec_pago: str
    cuponbono: str
    residual: str
    obsprox_pago: str
    tipo_moneda: int
    tipo: str
    currentyield: str
    paridad: str
    diasrestantes: int
    grupo_cupon: str
    descripcion_moneda: str


class FlujoItem(BaseModel):
    """Projected cash flow item."""
    codigoespeciebono: str
    fecha: str
    vr: float
    renta: float
    amort: float
    rentaamort: str
    total: float
    tipo_moneda: int


class FlujoProyectadoResponse(BaseModel):
    """Response from /bonos/flujoproyectado endpoint."""
    tabla: List[BonoDetalle]
    excluidos: List
    flujo: List[FlujoItem]
