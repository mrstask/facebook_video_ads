import sqlalchemy as sa

TABLE_NAME = 'stask_meta'

metadata = sa.MetaData()
# todo create database and paste my connection data
connection = {'user': 'py4seo', 'database': 'library', 'host': '46.30.164.249', 'password': 'PY1111forSEO'}
dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**connection)
engine = sa.create_engine(dsn)
metadata.bind = engine


parse_results = sa.Table(
    TABLE_NAME, metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('url', sa.String),
    sa.Column('category', sa.Text),
    sa.Column('checked', sa.Boolean, default=False),
    )

if __name__ == '__main__':
    # metadata.drop_all()
    metadata.create_all()