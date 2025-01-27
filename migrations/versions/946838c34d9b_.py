"""empty message

Revision ID: 946838c34d9b
Revises: d41c15859479
Create Date: 2024-07-25 10:31:59.460622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946838c34d9b'
down_revision = 'd41c15859479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name_people', sa.String(length=252), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('name_people')

    # ### end Alembic commands ###
