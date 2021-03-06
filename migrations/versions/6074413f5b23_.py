"""empty message

Revision ID: 6074413f5b23
Revises: e0eb4141ee44
Create Date: 2018-10-18 21:01:01.916205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6074413f5b23'
down_revision = 'e0eb4141ee44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('token', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
