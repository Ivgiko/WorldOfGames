from sqlalchemy import create_engine, text
import os

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://user:userpassword@db:3306/game_scores')
engine = create_engine(DATABASE_URL)


def add_score(difficulty):
    score_value = (difficulty * 3) + 5

    try:
        with engine.connect() as connection:
            # Check if a score already exists
            result = connection.execute(text("SELECT score FROM users_scores LIMIT 1"))
            existing_score = result.scalar()

            if existing_score is not None:
                # Update the score by adding the new score
                new_score = existing_score + score_value
                query = text("UPDATE users_scores SET score = :new_score")
                connection.execute(query, {"new_score": new_score})
            else:
                # Insert the initial score if no score exists
                query = text("INSERT INTO users_scores (score) VALUES (:score_value)")
                connection.execute(query, {"score_value": score_value})

            # Commit the transaction
            connection.commit()

    except Exception as e:
        print(f"Error occurred while adding score to the database: {str(e)}")
