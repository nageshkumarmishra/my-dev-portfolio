from app.db import db
# Employee model representing a single employee record in the database
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)   # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Employee name
    department = db.Column(db.String(100), nullable=False) # Department name

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        Useful for serializing to JSON in API responses.
        """
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department
        }