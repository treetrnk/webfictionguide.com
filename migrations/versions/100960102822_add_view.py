"""Add View

Revision ID: 100960102822
Revises: 95380252bed1
Create Date: 2020-03-14 07:08:42.653625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100960102822'
down_revision = '95380252bed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fiction_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=15), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['fiction_id'], ['fiction.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('view')
    # ### end Alembic commands ###
