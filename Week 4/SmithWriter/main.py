import sys
from engine import BlogGenerator
from database import connect_to_database

db = connect_to_database()


def main():
    if len(sys.argv) < 2:
        print("Please provide a blog topic as a command line argument")
        print('Usage: python main.py "Your blog topic"')
        sys.exit(1)

    # Get the blog topic from command line argument
    topic = " ".join(sys.argv[1:])

    # Initialize blog generator
    blog_generator = BlogGenerator(topic)

    # Generate blog
    result = blog_generator.create_blog()

    # Store blog content in MongoDB if generation was successful
    if result:
        try:
            # Insert blog content into blogs collection
            inserted_doc = db.blogs.insert_one(blog_generator.blog_content)
            print(f"Blog content saved to database with id: {inserted_doc.inserted_id}")
            return inserted_doc.inserted_id
        except Exception as e:
            print(f"Error saving to database: {str(e)}")
            return None
    else:
        print("Error generating blog:", result.get("error", "Unknown error"))
        return None


if __name__ == "__main__":
    main()
