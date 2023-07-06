
# Delhi Munchies: The Canteen Chronicle

This command-line application is designed to manage the snack inventory of the canteen and keep track of sales. It allows canteen staff to add, remove, and update snacks in the inventory, as well as record sales.

## Features

- **Snack Inventory**: Add, remove, and update snacks in the inventory. Each snack has a unique ID, name, price, and availability status.

- **User Interaction**: The application provides a menu-driven interface for canteen staff to perform various tasks:
  - Add a snack to the inventory.
  - Remove a snack from the inventory.
  - Update the availability of a snack.

- **Sales Records**: The application keeps track of snacks sold. Staff can enter the snack's ID when a sale is made, and the application updates the inventory and sales records accordingly.

- **Error Handling**: The application handles invalid inputs and edge cases to ensure data integrity. For example, it prevents selling a snack that is unavailable and checks for valid inputs during snack addition.

## Prerequisites

- Python 

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/DishaGup/Delhi-Munchies.git
   ```


3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the application:

   ```shell
   python main.py
   ```

## Usage

- Follow the menu prompts to perform various actions:
  - Add a snack: Enter the snack details (ID, name, price, availability) to add it to the inventory.
  - Remove a snack: Enter the snack ID to remove it from the inventory.
  - Update snack availability: Enter the snack ID and the new availability status to update it.
  - Sell a snack: Enter the snack ID to record a sale.

- Use the option to exit the application when done.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

