from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(
        customer: dict[str, str] | Customer,
        product: str,
    ) -> None:
        if isinstance(customer, Customer):
            customer_name = customer.name
        else:
            customer_name = customer.get("name")
        print(f"Cinema bar sold {product} to {customer_name}.")
