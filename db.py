import sqlalchemy as sa

TABLE_NAME = 'stask_meta'

metadata = sa.MetaData()
# todo create database and paste my connection data
connection = {'user': '', 'database': '', 'host': '', 'password': ''}
dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**connection)
engine = sa.create_engine(dsn)
metadata.bind = engine



parse_results = sa.Table(
    TABLE_NAME, metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('campaign name', sa.String),
    sa.Column('adgroup', sa.String),
    sa.Column('description', sa.String),
    sa.Column('page_id', sa.String),
    sa.Column('link_video', sa.String),
    sa.Column('audience_name', sa.String),
    sa.Column('campaign_id', sa.String),
    sa.Column('custom_audience_id', sa.String),
    sa.Column('add_users_mk', sa.Boolean, default=False),
    sa.Column('checked', sa.Boolean),
    )

if __name__ == '__main__':
    # metadata.drop_all()
    metadata.create_all()