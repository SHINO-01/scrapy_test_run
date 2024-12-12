import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
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
        session = self.Session()

        # Fetch the downloaded image path
        images = adapter.get('images', [])
        if images:
            adapter['image_path'] = images[0]['path']
        else:
            adapter['image_path'] = None

        # Save data into the database
        product = Product(
            title=adapter.get('title'),
            price=adapter.get('price'),
            image_url=adapter.get('image_urls', [None])[0],
            product_url=adapter.get('product_url'),
            image_path=adapter.get('image_path')
        )
        session.add(product)
        session.commit()
        session.close()
        return item

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # Return the image filename directly
        image_guid = request.url.split('/')[-1]  # Use the original image filename
        return f"{image_guid}"

