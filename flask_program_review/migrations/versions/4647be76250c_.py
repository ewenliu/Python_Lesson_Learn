"""empty message

Revision ID: 4647be76250c
Revises: 8bf01e7651be
Create Date: 2019-11-10 17:04:57.149613

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4647be76250c'
down_revision = '8bf01e7651be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'post_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_constraint('highlight_post_ibfk_1', 'highlight_post', type_='foreignkey')
    op.create_foreign_key(None, 'highlight_post', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'highlight_post', type_='foreignkey')
    op.create_foreign_key('highlight_post_ibfk_1', 'highlight_post', 'post', ['post_id'], ['id'], ondelete='CASCADE')
    op.alter_column('comment', 'post_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###
