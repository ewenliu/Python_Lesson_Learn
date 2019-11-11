"""empty message

Revision ID: 85c2ddffa1c3
Revises: d31df1bf0688
Create Date: 2019-11-02 18:04:48.811086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85c2ddffa1c3'
down_revision = 'd31df1bf0688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('front_user', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.drop_index('telephone', table_name='front_user')
    op.drop_column('front_user', 'telephone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('telephone', mysql.VARCHAR(length=11), nullable=False))
    op.create_index('telephone', 'front_user', ['telephone'], unique=True)
    op.alter_column('front_user', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###
