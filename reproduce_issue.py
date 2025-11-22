
from App import app, db, bcrypt
from App.models import User
from flask_login import current_user

def reproduce():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use in-memory DB for testing
    
    with app.app_context():
        db.create_all()
        
        # Create a test user
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(
            username='testuser',
            email='test@example.com',
            password=hashed_password,
            name='Test',
            lname='User',
            dob=None # Assuming nullable or default handled, checking model... dob has default
        )
        db.session.add(user)
        db.session.commit()
        
        with app.test_client() as client:
            # Test Login
            print("Attempting login...")
            response = client.post('/login', data={
                'email_username': 'testuser',
                'password': 'password'
            }, follow_redirects=True)
            
            if response.status_code == 200:
                # Check if we are redirected to home or if we are logged in
                # Since we are using follow_redirects=True, we should check the content or current_user
                # However, current_user proxy might not work outside request context easily without some tricks
                # But inside the with block it should work if we access it via the client session or by checking the page content
                
                if b'Login Unsuccessful' in response.data:
                    print("Login Failed: Flash message found.")
                elif b'Log Out' in response.data or b'Account' in response.data: # Assuming these links appear when logged in
                     print("Login Successful: Found 'Log Out' or 'Account' in response.")
                else:
                    # Let's check if we are on the home page
                    if b'Home' in response.data:
                         print("Login Successful: Redirected to Home.")
                    else:
                         print("Login Status Unclear. Response data snippet:")
                         print(response.data[:500])
            else:
                print(f"Login Request Failed with status code: {response.status_code}")

            # Test Logout
            print("\nAttempting logout...")
            response = client.get('/logout', follow_redirects=True)
            
            if response.status_code == 200:
                if b'Sign In' in response.data or b'Login' in response.data:
                    print("Logout Successful: Found 'Sign In' or 'Login' in response.")
                else:
                    print("Logout Status Unclear. Response data snippet:")
                    print(response.data[:500])
            else:
                print(f"Logout Request Failed with status code: {response.status_code}")

if __name__ == '__main__':
    reproduce()
