class Product {
  String name = 'TV';
  double price = 24999.99;
  int quantity = 1;

  String get Name {
    print(name);
    return this.name;
  }

  double get Price {
    print(price);
    return this.price;
  }

  int get Quantity {
    print(quantity);
    return this.quantity;
  }
}

void main() {
  Product product = Product();
  product.Name;
  product.Price;
  product.Quantity;
}
