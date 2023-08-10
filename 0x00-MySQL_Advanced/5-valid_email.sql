-- Create a Trigger to Reset valid_email When Email Changes
DELIMITER //
CREATE TRIGGER ResetValidEmail
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
