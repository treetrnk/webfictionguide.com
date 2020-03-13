"""Add subscriber

Revision ID: 95380252bed1
Revises: 1d70e65c8c96
Create Date: 2020-03-13 06:56:49.139681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95380252bed1'
down_revision = '1d70e65c8c96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('first_name', sa.String(length=75), nullable=True),
    sa.Column('last_name', sa.String(length=75), nullable=True),
    sa.Column('comment', sa.String(length=1000), nullable=True),
    sa.Column('sub_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriber')
    # ### end Alembic commands ###