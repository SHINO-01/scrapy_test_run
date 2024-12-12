import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from itemadapter import ItemAdapter

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    product_url = Column(String, nullable=True)
    image_path = Column(String, nullable=True)

class PracticeScrapPipeline:
    def __init__(self):
        DATABASE_URL = "postgresql://scrapy_user:scrapy_pass@postgres:5432/scrapyDB"
        self.engine = sqlalchemy.create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        image_paths = adapter.get('images', [])
        if image_paths:
            adapter['image_path'] = image_paths[0]['path']
        else:
            adapter['image_path'] = None

        session = self.Session()
        product = Product(
            title=adapter['title'],
            price=adapter['price'],
            image_url=adapter['image_url'],
            product_url=adapter['product_url'],
            image_path=adapter['image_path']
        )
        session.add(product)
        session.commit()
        session.close()
        return item
