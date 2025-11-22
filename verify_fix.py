
from App import app, db, bcrypt
from App.models import User
from flask_login import current_user

def verify_fix():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
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
            dob=None
        )
        db.session.add(user)
        db.session.commit()
        
        with app.test_client() as client:
            print("1. Testing Unauthenticated Access to Protected Route (/router)...")
            response = client.get('/router', follow_redirects=True)
            
            # Should be redirected to login page
            if b'Sign In' in response.data or b'Login' in response.data:
                print("PASS: Unauthenticated access redirected to login.")
            else:
                print("FAIL: Unauthenticated access NOT redirected to login.")
                print(response.data[:500])

            print("\n2. Testing Authenticated Access...")
            # Login
            client.post('/login', data={
                'email_username': 'testuser',
                'password': 'password'
            }, follow_redirects=True)
            
            # Access protected route
            response = client.get('/router', follow_redirects=True)
            
            if b'Codemon' in response.data or b'Logout' in response.data: # Landing_page has Codemon title and Logout button
                 print("PASS: Authenticated access successful.")
            else:
                 print("FAIL: Authenticated access failed.")
                 print(response.data[:500])

            print("\n3. Testing Logout...")
            client.get('/logout', follow_redirects=True)
            
            # Access protected route again
            response = client.get('/router', follow_redirects=True)
            
            if b'Sign In' in response.data or b'Login' in response.data:
                print("PASS: Access denied after logout.")
            else:
                print("FAIL: Access still allowed after logout.")

if __name__ == '__main__':
    verify_fix()
