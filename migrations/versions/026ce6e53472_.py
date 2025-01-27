"""empty message

Revision ID: 026ce6e53472
Revises: b784a6aba06a
Create Date: 2024-07-24 13:47:58.694886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '026ce6e53472'
down_revision = 'b784a6aba06a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people_favorite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people_favorite',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('User_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['user.id'], name='people_favorite_User_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='people_favorite_pkey')
    )
    # ### end Alembic commands ###
