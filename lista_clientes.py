class Lista_Clientes():
    def __init__(self)-> None:
        self.head = None
        self.last = None

    def add(self, nombre):
        nuevo_cliente = Nodo_Cliente(nombre)
        
        if self.head is None:
            self.head = nuevo_cliente
            self.last = nuevo_cliente
        
        else:
            self.last.next = nuevo_cliente
            nuevo_cliente.prev = self.last
            self.last = nuevo_cliente

    def imprimir(self):
        cliente_auxiliar = self.head;

        while cliente_auxiliar != None:
            print(cliente_auxiliar.nombre)
            cliente_auxiliar = cliente_auxiliar.next
    
    def search(self, nombre):
        cliente_auxiliar = self.head

        while cliente_auxiliar != None:
            if cliente_auxiliar.nombre == nombre:
                return cliente_auxiliar
            cliente_auxiliar = cliente_auxiliar.next
        
        return None

class Nodo_Cliente():
    def __init__(self, nombre) -> None:
        self.nombre = nombre;
        self.next = None
        self.prev = None
        self.lista_hojas = Lista_Hojas()


class Lista_Hojas():
    def __init__(self) -> None:
        self.head = None
        self.last = None
    
    def add(self, contenido):
        nueva_hoja = Nodo_Hoja(contenido);

        if self.head is None:
            self.head = nueva_hoja
            self.last = nueva_hoja
        
        else:
            self.last.next = nueva_hoja
            nueva_hoja.prev = self.last
            self.last = nueva_hoja


class Nodo_Hoja():
    def __init__(self, contenido) -> None:
        self.contenido = contenido
        self.next = None
        self.prev = None

# Proba
lista_clientes = Lista_Clientes()
lista_clientes.add("Faviola")
lista_clientes.add("Katherin")
lista_clientes.add("Angely")

cliente = lista_clientes.search("Katherin")
cliente.lista_hojas.add("La hora usasavasdff")

lista_clientes.imprimir()
