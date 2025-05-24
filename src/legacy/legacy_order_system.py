customers = []
products = []
orders = []
users = []
current_user = None
lang = "pt"

def add_user(u, p, t):
    users.append({"username": u, "password": p, "type": t})
    print(f"Usuário {u} criado com sucesso.")

def login(u, p):
    global current_user
    for user in users:
        if user["username"] == u and user["password"] == p:
            current_user = user
            if lang == "pt":
                print(f"Bem-vindo, {u}!")
            else:
                print(f"Welcome, {u}!")
            return True
    if lang == "pt":
        print("Credenciais inválidas.")
    else:
        print("Invalid credentials.")
    return False

def register_customer(name, address, email):
    if current_user is None or current_user["type"] not in ["admin", "vendedor"]:
        if lang == "pt":
            print("Sem permissão para cadastrar clientes.")
        else:
            print("No permission to register customers.")
        return
    
    customers.append({"name": name, "address": address, "email": email, "orders": []})
    if lang == "pt":
        print(f"Cliente {name} registrado com sucesso.")
    else:
        print(f"Customer {name} registered successfully.")

def add_product(n, c, p, q):
    if current_user is None or current_user["type"] != "admin":
        if lang == "pt":
            print("Sem permissão para adicionar produtos.")
        else:
            print("No permission to add products.")
        return
    
    products.append({"name": n, "category": c, "price": p, "quantity": q})
    if lang == "pt":
        print(f"Produto {n} adicionado com sucesso.")
    else:
        print(f"Product {n} added successfully.")

def create_order(customer_name, items, quantities, payment_type):
    if current_user is None:
        if lang == "pt":
            print("É necessário fazer login para criar pedidos.")
        else:
            print("Login required to create orders.")
        return
    
    customer_idx = -1
    for i, cust in enumerate(customers):
        if cust["name"] == customer_name:
            customer_idx = i
            break
    
    if customer_idx == -1:
        if lang == "pt":
            print(f"Cliente {customer_name} não encontrado.")
        else:
            print(f"Customer {customer_name} not found.")
        return
    
    total = 0
    order_items = []
    
    for i in range(len(items)):
        product_name = items[i]
        qty = quantities[i]
        
        product_idx = -1
        for j, prod in enumerate(products):
            if prod["name"] == product_name:
                product_idx = j
                break
        
        if product_idx == -1:
            if lang == "pt":
                print(f"Produto {product_name} não encontrado.")
            else:
                print(f"Product {product_name} not found.")
            continue
        
        if products[product_idx]["quantity"] < qty:
            if lang == "pt":
                print(f"Quantidade insuficiente de {product_name} em estoque.")
            else:
                print(f"Insufficient quantity of {product_name} in stock.")
            continue
        
        products[product_idx]["quantity"] -= qty
        
        item_price = products[product_idx]["price"] * qty
        
        if products[product_idx]["category"] == "eletrônicos":
            item_price *= 0.9
        
        total += item_price
        
        order_items.append({
            "product": product_name,
            "quantity": qty,
            "price": products[product_idx]["price"],
            "total": item_price
        })
    
    discount = 0
    if total > 1000:
        discount = total * 0.05
        total -= discount
    
    tax = total * 0.1
    final_total = total + tax
    
    order = {
        "customer": customer_name,
        "items": order_items,
        "subtotal": total,
        "discount": discount,
        "tax": tax,
        "total": final_total,
        "payment_type": payment_type,
        "status": "pendente"
    }
    
    orders.append(order)
    customers[customer_idx]["orders"].append(len(orders) - 1)
    
    send_notification(customer_name, "novo_pedido", len(orders) - 1)
    
    if lang == "pt":
        print(f"Pedido criado para {customer_name} com total de {final_total}.")
    else:
        print(f"Order created for {customer_name} with total of {final_total}.")
    
    return len(orders) - 1

def update_order_status(order_index, new_status):
    if current_user is None or current_user["type"] not in ["admin", "vendedor"]:
        if lang == "pt":
            print("Sem permissão para atualizar status de pedidos.")
        else:
            print("No permission to update order status.")
        return
    
    if 0 <= order_index < len(orders):
        orders[order_index]["status"] = new_status
        
        customer_name = orders[order_index]["customer"]
        send_notification(customer_name, "status_atualizado", order_index)
        
        if lang == "pt":
            print(f"Status do pedido {order_index} atualizado para {new_status}.")
        else:
            print(f"Order {order_index} status updated to {new_status}.")
    else:
        if lang == "pt":
            print("Pedido não encontrado.")
        else:
            print("Order not found.")

def generate_report():
    if current_user is None:
        if lang == "pt":
            print("É necessário fazer login para gerar relatórios.")
        else:
            print("Login required to generate reports.")
        return
    
    if lang == "pt":
        print("Relatório de Pedidos:")
    else:
        print("Order Report:")
    
    for i, order in enumerate(orders):
        if lang == "pt":
            print(f"Pedido {i}:")
            print(f"  Cliente: {order['customer']}")
            print(f"  Itens:")
            for item in order['items']:
                print(f"    - {item['product']}: {item['quantity']} x {item['price']} = {item['total']}")
            print(f"  Subtotal: {order['subtotal']}")
            print(f"  Desconto: {order['discount']}")
            print(f"  Imposto: {order['tax']}")
            print(f"  Total: {order['total']}")
            print(f"  Forma de Pagamento: {order['payment_type']}")
            print(f"  Status: {order['status']}")
        else:
            print(f"Order {i}:")
            print(f"  Customer: {order['customer']}")
            print(f"  Items:")
            for item in order['items']:
                print(f"    - {item['product']}: {item['quantity']} x {item['price']} = {item['total']}")
            print(f"  Subtotal: {order['subtotal']}")
            print(f"  Discount: {order['discount']}")
            print(f"  Tax: {order['tax']}")
            print(f"  Total: {order['total']}")
            print(f"  Payment Method: {order['payment_type']}")
            print(f"  Status: {order['status']}")

def customer_order_history(customer_name):
    if current_user is None:
        if lang == "pt":
            print("É necessário fazer login para ver histórico de pedidos.")
        else:
            print("Login required to view order history.")
        return
    
    customer_idx = -1
    for i, cust in enumerate(customers):
        if cust["name"] == customer_name:
            customer_idx = i
            break
    
    if customer_idx == -1:
        if lang == "pt":
            print(f"Cliente {customer_name} não encontrado.")
        else:
            print(f"Customer {customer_name} not found.")
        return
    
    if lang == "pt":
        print(f"Histórico de Pedidos de {customer_name}:")
    else:
        print(f"Order History for {customer_name}:")
    
    for order_idx in customers[customer_idx]["orders"]:
        order = orders[order_idx]
        if lang == "pt":
            print(f"Pedido {order_idx}:")
            print(f"  Total: {order['total']}")
            print(f"  Status: {order['status']}")
        else:
            print(f"Order {order_idx}:")
            print(f"  Total: {order['total']}")
            print(f"  Status: {order['status']}")

def send_notification(customer_name, notification_type, order_index):
    for cust in customers:
        if cust["name"] == customer_name:
            email = cust["email"]
            if notification_type == "novo_pedido":
                if lang == "pt":
                    print(f"Notificação enviada para {email}: Novo pedido criado (Pedido #{order_index}).")
                else:
                    print(f"Notification sent to {email}: New order created (Order #{order_index}).")
            elif notification_type == "status_atualizado":
                status = orders[order_index]["status"]
                if lang == "pt":
                    print(f"Notificação enviada para {email}: Status do pedido #{order_index} atualizado para {status}.")
                else:
                    print(f"Notification sent to {email}: Order #{order_index} status updated to {status}.")
            break

def change_language(language):
    global lang
    if language in ["pt", "en"]:
        lang = language
        if lang == "pt":
            print("Idioma alterado para Português.")
        else:
            print("Language changed to English.")
    else:
        if lang == "pt":
            print("Idioma não suportado.")
        else:
            print("Language not supported.")

if __name__ == "__main__":
    add_user("admin", "admin123", "admin")
    add_user("vendedor", "vend123", "vendedor")
    
    login("admin", "admin123")
    
    register_customer("João Silva", "Rua A, 123", "joao@example.com")
    register_customer("Maria Souza", "Rua B, 456", "maria@example.com")
    
    add_product("Smartphone", "eletrônicos", 1500.0, 10)
    add_product("Notebook", "eletrônicos", 3000.0, 5)
    add_product("Teclado", "acessórios", 100.0, 20)
    add_product("Mouse", "acessórios", 50.0, 30)
    
    create_order("João Silva", ["Smartphone", "Teclado"], [1, 2], "cartão de crédito")
    create_order("Maria Souza", ["Notebook", "Mouse"], [1, 1], "boleto")
    
    update_order_status(0, "pago")
    
    generate_report()
    
    customer_order_history("João Silva")
    
    change_language("en")
    generate_report()