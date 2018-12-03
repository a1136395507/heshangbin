"""empty message

Revision ID: 91907ff9a1a2
Revises: 
Create Date: 2018-10-18 18:36:50.895225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91907ff9a1a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wheel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wheel')
    # ### end Alembic commands ###