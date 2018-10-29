import sqlalchemy as sa

TABLE_NAME = 'fb_campaigns'
TABLE_NAME_2 = 'fb_audience'


metadata = sa.MetaData()
connection = {'user': 'stask', 'database': 'myproject', 'host': 'localhost', 'password': 'trololo123'}
dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**connection)
engine = sa.create_engine(dsn)
metadata.bind = engine

campaigns = sa.Table(
    TABLE_NAME, metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('campaign_name', sa.String),
    sa.Column('adgroup', sa.String),
    sa.Column('description', sa.String),
    sa.Column('link_video', sa.String),
    sa.Column('destination_url', sa.String),
    sa.Column('campaign_id', sa.String),
    sa.Column('custom_audience_id', sa.String),
    sa.Column('add_users_mk', sa.Boolean, default=False),
    sa.Column('ad_set_id', sa.String),
    sa.Column('video_id', sa.String),
    sa.Column('video_creation_id', sa.String),
    sa.Column('creative_group_id', sa.String),
    sa.Column('done', sa.Boolean, default=False),
    )

audience = sa.Table(
    TABLE_NAME_2, metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('audience_name', sa.String),
    sa.Column('email', sa.String),
    sa.Column('phone', sa.String),
    sa.Column('done', sa.Boolean, default=False),
    )

if __name__ == '__main__':
    # metadata.drop_all()
    metadata.create_all()