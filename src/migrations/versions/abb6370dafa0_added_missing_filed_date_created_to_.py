"""added missing filed=> date_created to tasks table

Revision ID: abb6370dafa0
Revises: 3a23291a1d46
Create Date: 2024-08-22 12:43:13.635637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abb6370dafa0'
down_revision = '3a23291a1d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###
