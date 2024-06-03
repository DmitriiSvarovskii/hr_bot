"""1 migrations

Revision ID: 03e7be3529a7
Revises: 
Create Date: 2024-06-03 14:58:02.370058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03e7be3529a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('admin', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('result_tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('e', sa.Integer(), nullable=False),
    sa.Column('i', sa.Integer(), nullable=False),
    sa.Column('s', sa.Integer(), nullable=False),
    sa.Column('n', sa.Integer(), nullable=False),
    sa.Column('t', sa.Integer(), nullable=False),
    sa.Column('f', sa.Integer(), nullable=False),
    sa.Column('j', sa.Integer(), nullable=False),
    sa.Column('p', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_result_tests_id'), 'result_tests', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_result_tests_id'), table_name='result_tests')
    op.drop_table('result_tests')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###