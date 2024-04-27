class InMemoryDB:
  # Create constructor for the InMemoryDB class
  def __init__(self):
    self.db = {}
    self.transaction = False
    self.commited = False
    self.temp_b = {}

  # Create a function for when user starts a new transaction
  def begin_transaction(self):
    if not self.transaction:
      self.transaction = True
      self.temp_db = {}
      print("Transaction started...")
    else:
      raise Exception("Error: Transaction already in progress")
    
  # Create a function to update the value of an existing key, or create a new key with value if key doesn't exist
  def put(self, key, value):
    if self.transaction:
      self.temp_db[key] = value
      self.commited = False
      print("The value " + str(value) + " has been created/updated for " + key + ".")
    else:
      raise Exception("Error: No transaction in progress to create/update a key")
    
  # Create a function to apply changes made within the transaction to the main state
  def commit(self):
    if self.transaction:
      self.commited = True
      self.transaction = False
      self.db.update(self.temp_db)
      self.temp_db = {}
      print("Updates have been applied successfully")
    else:
      raise Exception("Error: No transaction in progress to commit")
    
  # Create a funtion to return the value associated with the key or null if the key doesn’t exist
  def get(self, key):
    if key in self.db:
      print("Value retrieved for " + key + ": " + str(self.db[key]))
    else:
      print("Value retrieved for " + key + ": " + str(None))
  
  # Create a function to abort all the changes made within the transaction
  def rollback(self):
    if self.transaction:
      self.transaction = False
      self.temp_db = {}
      print("All changes within transaction have been aborted")
    else:
      raise Exception("Error: No transaction in progress to rollback")

def main():
    db = InMemoryDB()

    # Test 1: Attempt to put a value without starting a transaction
    print("\nTest 1: Attempt to put a value without a transaction in progress")
    try:
        db.put("A", 10)
    except Exception as e:
        print(e)  # Expected: No transaction in progress to create/update a key
    print("DB: " + str(db.db))

    # Test 2: Start a transaction, put a value, and try to get value without commiting
    print("\nTest 2: Start a transaction, put a value of 10 to key A, and try to get value without commiting")
    try:
      db.begin_transaction()
      db.put("A", 10)
      db.get("A")  # This should output None("NULL") anything since changes are not committed
    except Exception as e:
      print(e)
    print("DB: " + str(db.db))
    
    # Test 3: Commit the transaction and check the value
    print("\nTest 3: Commit transaction from Test 2 and get/check the value")
    try:
        db.commit()
        db.get("A")  # Expected output: Value: 10
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 4: Start another transaction and update the same key without commiting
    print("\nTest 4: Start another transaction, update same key to have value 20, get value WITHOUT commiting")
    try:
        db.begin_transaction()
        db.put("A", 20)
        db.get("A")  # This should output the updated value 10
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 5: Update the same key and then commit
    print("\nTest 5: Update same key to have value 20, get value AFTER commiting")
    try:
        db.put("A", 20)
        db.commit()
        db.get("A")  # This should output the updated value 20
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 6: Commiting when there is no transaction in progress
    print("\nTest 6: Commiting when there is no transaction in progress")
    try:
        db.commit()
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 7: Rollback when there is no transaction in progress
    print("\nTest 7: Try to rollback when there is no transaction in progress")
    try:
        db.rollback()
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 8: Begin transaction, create new keys D and E, rollback transaction, then check values
    print("\nTest 8: Begin transaction, create new keys D and E, rollback transaction, then check values")
    try:
        db.begin_transaction()
        db.put("D", 12)
        db.put("E", 74)
        db.rollback()
        db.get("D")
        db.get("E")
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 9: Begin transaction and add multiple keys, and check each value without comitting any
    print("\nTest 9: Begin transaction and add multiple keys, and check each value without comitting anything")
    try:
        db.begin_transaction()
        db.put("B", 30)
        db.put("C", 7)
        db.put("D", 12)
        db.put("E", 74)
        db.get("B")
        db.get("C")
        db.get("D")
        db.get("E")
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 10: Add multiple keys, commit, and check each value
    print("\nTest 10: Add multiple keys, commit, and check each value")
    try:
        db.put("B", 30)
        db.put("C", 7)
        db.put("D", 12)
        db.put("E", 74)
        db.commit()
        db.get("B")
        db.get("C")
        db.get("D")
        db.get("E")
    except Exception as e:
        print(e)
    print("DB: " + str(db.db))

    # Test 11: Try to get value of key that doesn't exist in DB yet
    print("\nTest 11: Try to get value of key that doesn't exist in DB yet, in this case, we try F")
    db.get("F")  # Expected output: None
    print("DB: " + str(db.db))

    # Test 12: Start a new transaction when one is already in progress
    print("\nTest 12: Start a new transaction when one is already in progress")
    try:
        db.begin_transaction()
        db.begin_transaction()
    except Exception as e:
        print(e)  # Expected: Transaction already in progress
    print("DB: " + str(db.db))

    print("\nEnd of tests.")

if __name__ == "__main__":
    main()