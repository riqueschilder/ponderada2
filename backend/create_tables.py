from app import app, db, User

with app.app_context():
    db.create_all()

    # Adicionar usuário de teste
    test_user = User(username='teste', password='teste123')
    db.session.add(test_user)
    db.session.commit()

    print("Tabelas criadas e usuário de teste adicionado.")
