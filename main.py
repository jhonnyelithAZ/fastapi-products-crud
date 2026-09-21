from fastapi import FastAPI

app = FastAPI()

# Base de datos en memoria para los productos
productos = []

# 1) CRUD Productos: Crear (POST)
@app.post("/productos")
def create_producto(producto: dict):
    productos.append(producto)
    return producto

# 2) y 3) Buscar Productos con Query Params (GET)
@app.get("/productos")
def get_productos(category: str = None, limit: int = None):
    # Empezamos con la lista completa
    resultado = productos
    
    # Query Param: Búsqueda por categoría
    if category:
        resultado = [p for p in resultado if p.get("Category") == category]
        
    # Query Param: Limitar cantidad
    if limit:
        resultado = resultado[:limit]
        
    return resultado

#  CRUD Productos: Actualizar (PUT)
@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, updated_producto: dict):
    global productos
    for index, p in enumerate(productos):
        if p.get("id") == producto_id:
            productos[index] = updated_producto
            return {"message": f"Producto con id {producto_id} actualizado.", "producto": updated_producto}
            
    return {"error": "Producto no encontrado"}

# CRUD Productos: Eliminar (DELETE)
@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    global productos
    productos = [p for p in productos if p.get("id") != producto_id]
    return {"message": f"Producto con id {producto_id} eliminado."}