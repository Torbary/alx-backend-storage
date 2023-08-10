-- Create a Trigger to Decrease Item Quantity After Adding New Order
DELIMITER //
CREATE TRIGGER DecreaseItemQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
